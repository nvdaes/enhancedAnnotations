# -*- coding: UTF-8 -*-

# enhancedAnnotations: add ability to move to additional details and go back to original object
# https://github.com/nvaccess/nvda/issues/13940
# Copyright (C) 2022-2023 Noelia Ruiz Martínez, NV Access
# Implementation of PR: https://github.com/nvaccess/nvda/pull/14389
# Released under GPL 2

from typing import Callable

import api
import ui
import speech
import textInfos
import inputCore
import globalPluginHandler
from globalCommands import commands
from logHandler import log
from browseMode import BrowseModeDocumentTreeInterceptor
from controlTypes import OutputReason
from NVDAObjects import NVDAObject
from scriptHandler import script
import addonHandler

from .skipTranslation import translate

addonHandler.initTranslation()

_: Callable[[str], str]


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = inputCore.SCRCAT_BROWSEMODE

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
		objWithAnnotation = commands._getNvdaObjWithAnnotationUnderCaret()
		if not objWithAnnotation:
			# Translators: message given when there is no annotation details for the reportDetailsSummary script.
			ui.message(translate("No additional details"))
			return

		if (
			commands._annotationNav.lastReported
			and objWithAnnotation == commands._annotationNav.lastReported.origin
			and None is not commands._annotationNav.lastReported.indexOfLastReportedSummary
		):
			# This origin was the last
			targetIndex = commands._annotationNav.lastReported.indexOfLastReportedSummary
			target = list(objWithAnnotation.annotations.targets)[targetIndex]
		else:
			target = next(iter(objWithAnnotation.annotations.targets))
		self._moveToObject(target.targetObject)
		commands._annotationNav.priorOrigins.append(objWithAnnotation)
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
		"""Go to the annotation subject for the single character under the caret or the object with
		system focus.
		@note: See related script_reportDetailsSummary
		"""
		log.debug("Return to annotation parent.")
		if not commands._annotationNav.priorOrigins:
			# Translators: message given when there is no annotation details for the reportDetailsSummary script.
			ui.message(_("No annotation subject present"))
			return
		annotationParent = commands._annotationNav.priorOrigins.pop()
		self._moveToObject(annotationParent)
		return
