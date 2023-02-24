# -*- coding: UTF-8 -*-

# enhancedAnnotations: add ability to move to additional details and go back to original object
# https://github.com/nvaccess/nvda/issues/13940
# Copyright (C) 2022-2023 Noelia Ruiz Martínez, NV Access
# Implementation of PR: https://github.com/nvaccess/nvda/pull/14389 
# Released under GPL 2

from typing import Callable

import api
import config
import ui
import speech
import textInfos
import inputCore
import globalPluginHandler
from annotation import (
	_AnnotationNavigation,
	_AnnotationNavigationNode,
)
from logHandler import log
from browseMode import BrowseModeDocumentTreeInterceptor
from controlTypes import OutputReason
from NVDAObjects import NVDAObject
from scriptHandler import script
import addonHandler

addonHandler.initTranslation()

_: Callable[[str], str]


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = inputCore.SCRCAT_BROWSEMODE

	def _getNvdaObjWithAnnotationUnderCaret(self) -> Optional[NVDAObject]:
		"""If it has an annotation, get the NVDA object for the single character under the caret or the object
		with system focus.
		@note: It is tempting to try to report any annotation details that exists in the range formed by prior
			and current location. This would be a new paradigm in NVDA, and may feel natural when moving by line
			to be able to more quickly have the 'details' reported. However, there may be more than one 'details
			relation' in that range, and we don't yet have a way for the user to select which one to report.
			For now, we minimise this risk by only reporting details at the current location.
		"""
		try:
			# Common cases use Caret Position: vbuf available or object supports text range
			# Eg editable text, or regular web content
			# Firefox and Chromium support this even in a button within a role=application.
			caret: textInfos.TextInfo = api.getCaretPosition()
		except RuntimeError:
			log.debugWarning("Unable to get the caret position.", exc_info=True)
			return None
		caret.expand(textInfos.UNIT_CHARACTER)
		objAtStart: NVDAObject = caret.NVDAObjectAtStart
		_isDebugLogCatEnabled = bool(config.conf["debugLog"]["annotations"])
		if _isDebugLogCatEnabled:
			log.debug(f"Trying with nvdaObject : {objAtStart}")

		if objAtStart.detailsSummary:
			log.debug(f"NVDAObjectAtStart of caret has details: {objAtStart.detailsSummary}")
			return objAtStart
		elif api.getFocusObject():
			# If fetching from the caret position fails, try via the focus object
			# This case is to support where there is no virtual buffer or text interface and a caret position can
			# not be fetched.
			# There may still be an object with focus that has details.
			# There isn't a known test case for this, however there isn't a known downside to attempt this.
			focus = api.getFocusObject()
			if _isDebugLogCatEnabled:
				log.debug(f"Trying focus object: {focus}")

			if focus.detailsSummary:
				if _isDebugLogCatEnabled:
					log.debug("focus object has details, able to proceed")
				return focus

		if _isDebugLogCatEnabled:
			log.debug("no details annotation found")
		return None

	_annotationNav = AnnotationNavigation()

	@script(
		gesture="kb:NVDA+alt+d",
		description=_(
			# Translators: the description for the reportDetailsSummary script.
			"Go to annotation details under the system caret."
		)
	)
	def script_goToAnnotation(self, gesture):
		"""Go to the annotation details for the single character under the caret or the object with
		system focus.
		@note: See related script_reportDetailsSummary
		"""
		log.debug("Go to annotation details at current location.")
		objWithAnnotation = self._getNvdaObjWithAnnotationUnderCaret()
		if not objWithAnnotation:
			# Translators: message given when there is no annotation details for the reportDetailsSummary script.
			ui.message(_("No annotation present"))
			return

		if (
			self._annotationNav.lastReported
			and objWithAnnotation == self._annotationNav.lastReported.origin
			and None is not self._annotationNav.lastReported.indexOfLastReportedSummary
		):
			# This origin was the last
			targetIndex = self._annotationNav.lastReported.indexOfLastReportedSummary
			target = list(objWithAnnotation.annotations.targets)[targetIndex]
		else:
			target = next(iter(objWithAnnotation.annotations.targets))
		# Translators: message given when navigating to annotation target.
		ui.message("Navigating to target")
		self._moveToObject(target.targetObject)
		self._annotationNav.priorOrigins.append(objWithAnnotation)
		return

	def _moveToObject(self, toObject: "NVDAObject"):
		focus = api.getFocusObject()
		treeInterceptor = focus.treeInterceptor
		if not isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) or treeInterceptor.passThrough:
			return
		info = treeInterceptor.makeTextInfo(toObject)
		forSelect = info.copy()
		forSelect.collapse()
		treeInterceptor._set_selection(forSelect, reason=OutputReason.QUICKNAV)
		self._reportInfoAfterMove(info)

	def _reportInfoAfterMove(self, info: "textInfos.TextInfo"):

		# See impl of browseMode.TextInfoQuickNavItem.report sometimes readUnit is provided:
		# It originates from using textInfos.UNIT_LINE for:
		# Table, list, edit, frame, notLinkBlock, landmark
		# See "Add quick navigation scripts" in source/browseMode.py:646
		speech.speakTextInfo(info, reason=OutputReason.QUICKNAV)

	@script(
		gesture="kb:NVDA+alt+shift+d",
		description=_(
			# Translators: the description for the script_popAnnotationStack script.
			"Return to annotation subject"
		)
	)
	def script_popAnnotationStack(self, gesture):
		"""Go to the annotation details for the single character under the caret or the object with
		system focus.
		@note: See related script_reportDetailsSummary
		"""
		log.debug("Return to annotation parent.")
		if not self._annotationNav.priorOrigins:
			# Translators: message given when there is no annotation details for the reportDetailsSummary script.
			ui.message(_("No annotation subject present"))
			return
		annotationParent = self._annotationNav.priorOrigins.pop()
		self._moveToObject(annotationParent)
		return
