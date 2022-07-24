# -*- coding: UTF-8 -*-

# enhancedAnnotations: add ability to move to additional details and go back to original object
# https://github.com/nvaccess/nvda/issues/13940
# Copyright (C) 2022 Noelia Ruiz Martínez
# Released under GPL 2

from typing import Callable

import api
import ui
import speech
import inputCore
import globalPluginHandler
from logHandler import log
from browseMode import BrowseModeDocumentTreeInterceptor
from controlTypes import OutputReason
from scriptHandler import script
import addonHandler

from skipTranslation import translate

addonHandler.initTranslations()

_: Callable[[str], str]


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = inputCore.SCRCAT_BROWSEMODE

	def __init__(self):
		super().__init__()
		self._lastObjWithDetails = None

	def terminate(self):
		self._lastObjWithDetails = None

	@script(
		# Translators: message presented in input help mode.
		description=_("Navigates to the details of the current position in browse mode"),
		gesture="kb:NVDA+alt+d"
	)
	def script_moveToRelatedDetails(self, gesture):
		focus = api.getFocusObject()
		treeInterceptor = focus.treeInterceptor
		if not isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) or treeInterceptor.passThrough:
			return
		curObj = treeInterceptor.currentNVDAObject
		if curObj.hasDetails:
			relatedDetails = curObj.detailsRelations
		else:
			# Message translated in NVDA's core.
			ui.message(translate("No additional details"))
			return
		for target in relatedDetails:
			info = treeInterceptor.makeTextInfo(target)
			info.collapse()
			treeInterceptor._set_selection(info, reason=OutputReason.QUICKNAV)
			speech.speakObject(treeInterceptor.currentNVDAObject, reason=OutputReason.QUICKNAV)
			self._lastObjWithDetails = curObj
			return

	@script(
		# Translators: message presented in input help mode.
		description=_("After navigating to additional details, moves back to the original position in browse mode"),
		gesture="kb:NVDA+shift+alt+d"
	)
	def script_moveBackToObjWithDetails(self, gesture):
		focus = api.getFocusObject()
		treeInterceptor = focus.treeInterceptor
		if not isinstance(treeInterceptor, BrowseModeDocumentTreeInterceptor) or treeInterceptor.passThrough:
			return
		if self._lastObjWithDetails is None:
			# Translators: message presented when there's no original object to go back from additional details.
			ui.message(_("No element with additional details to go back"))
			return
		try:
			info = treeInterceptor.makeTextInfo(self._lastObjWithDetails)
			info.collapse()
			treeInterceptor._set_selection(info, reason=OutputReason.QUICKNAV)
			speech.speakObject(treeInterceptor.currentNVDAObject, reason=OutputReason.QUICKNAV)
		except LookupError as e:
			log.debugWarning("enhancedAnnotations add-on: error moving to object with details", exc_info=True)
			raise e
