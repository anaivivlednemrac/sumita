#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on julio 02, 2023, at 22:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'prueba de sumacion'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\saezr\\OneDrive\\Escritorio\\prueba de sumacion 2\\prueba de sumacion.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0,1.0,1.0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
foto_excitadordetransferencia_pds = visual.ImageStim(
    win=win,
    name='foto_excitadordetransferencia_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
EIfotoPERRO_excitadordetransferencia_pds = visual.ImageStim(
    win=win,
    name='EIfotoPERRO_excitadordetransferencia_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
EISONIDO_excitadordetransferencia_pds = sound.Sound('A', secs=0.7, stereo=True, hamming=True,
    name='EISONIDO_excitadordetransferencia_pds')
EISONIDO_excitadordetransferencia_pds.setVolume(1.0)

# --- Initialize components for Routine "ITI" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "ESTIMULO_COMPUESTO_INHIBIDOR_pds" ---
foto_inhibidor_a_prueba_pds = visual.ImageStim(
    win=win,
    name='foto_inhibidor_a_prueba_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(1.0, 0.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
foto_excitadordetransferencia_pds_foto = visual.ImageStim(
    win=win,
    name='foto_excitadordetransferencia_pds_foto', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.0, 1.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
escalaexpectativa_estimulocompuestoinhibidor_pds = visual.TextStim(win=win, name='escalaexpectativa_estimulocompuestoinhibidor_pds',
    text='',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
slider_expectativa_estimulocompuestoinhibidor_pds = visual.Slider(win=win, name='slider_expectativa_estimulocompuestoinhibidor_pds',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco probable" , "Muy probable"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)

# --- Initialize components for Routine "ITI" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "ESTIMULO_COMPUESTO_NEUTRO_pds" ---
foto_estimulo_neutro_pds = visual.ImageStim(
    win=win,
    name='foto_estimulo_neutro_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(1.0, 0.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
foto_excitadordetransferencia_estimulocompuestoneutro_pds = visual.ImageStim(
    win=win,
    name='foto_excitadordetransferencia_estimulocompuestoneutro_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 1.0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
escalaexpectativa_estimulocompuestoneutro_pds = visual.TextStim(win=win, name='escalaexpectativa_estimulocompuestoneutro_pds',
    text='',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
slider_estimulocompuestoneutro_pds = visual.Slider(win=win, name='slider_estimulocompuestoneutro_pds',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco probable" , "Muy probable"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)

# --- Initialize components for Routine "ITI" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "ESTIMULO_EXCITATORIO_PDS" ---
foto_estimulo_condicionado_excitatorio_pds = visual.ImageStim(
    win=win,
    name='foto_estimulo_condicionado_excitatorio_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
escalaexpectativa_estimulocondicionadoexcitatorio_pds = visual.TextStim(win=win, name='escalaexpectativa_estimulocondicionadoexcitatorio_pds',
    text='',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_estimulocondicionadoexcitatorio_pds = visual.Slider(win=win, name='slider_estimulocondicionadoexcitatorio_pds',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco probable" , "Muy probable"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)
eifoto_estimulocondicionadoexcitatorio_pds = visual.ImageStim(
    win=win,
    name='eifoto_estimulocondicionadoexcitatorio_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
eisonido_estimulocondicionadoexcitatorio_pds = sound.Sound('A', secs=0.7, stereo=True, hamming=True,
    name='eisonido_estimulocondicionadoexcitatorio_pds')
eisonido_estimulocondicionadoexcitatorio_pds.setVolume(1.0)

# --- Initialize components for Routine "ITI" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "estimulo_compuesto_inhibidor_miedo_pds" ---
foto_inhibidor_a_prueba_miedo_pds = visual.ImageStim(
    win=win,
    name='foto_inhibidor_a_prueba_miedo_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
foto_excitador_de_transferencia_miedo_pds = visual.ImageStim(
    win=win,
    name='foto_excitador_de_transferencia_miedo_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
texto_escala_miedo_estimulo_compuesto_inhibidor_pds = visual.TextStim(win=win, name='texto_escala_miedo_estimulo_compuesto_inhibidor_pds',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
slider_miedo_estimulo_compuesto_inhibidor_pds = visual.Slider(win=win, name='slider_miedo_estimulo_compuesto_inhibidor_pds',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco miedo" , "Mucho miedo"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)

# --- Initialize components for Routine "ITI" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "estimulo_compuesto_neutro_miedo_pds" ---
foto_estimulo_compuesto_neutro_miedo_pds = visual.ImageStim(
    win=win,
    name='foto_estimulo_compuesto_neutro_miedo_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
foto_excitador_transferencia_miedo_pds = visual.ImageStim(
    win=win,
    name='foto_excitador_transferencia_miedo_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
texto_estimulo_compuesto_neutro_miedo_pds = visual.TextStim(win=win, name='texto_estimulo_compuesto_neutro_miedo_pds',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
slider_ = visual.Slider(win=win, name='slider_',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco miedo", "Mucho miedo"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)

# --- Initialize components for Routine "ITI" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "estimulo_excitatorio_miedo_pds" ---
foto_estimulo_excitatorio_miedo_pds = visual.ImageStim(
    win=win,
    name='foto_estimulo_excitatorio_miedo_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
texto_estimulo_excitatorio_miedo_pds = visual.TextStim(win=win, name='texto_estimulo_excitatorio_miedo_pds',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
slider_estimulo_condicionado_excitatorio_miedo_pds = visual.Slider(win=win, name='slider_estimulo_condicionado_excitatorio_miedo_pds',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=["Poco miedo", "Mucho miedo"], ticks=(1, 2, 3, 4, 5), granularity=1.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)
sonido_ei_estimulo_excitatorio_miedo_pds = sound.Sound('A', secs=0.7, stereo=True, hamming=True,
    name='sonido_ei_estimulo_excitatorio_miedo_pds')
sonido_ei_estimulo_excitatorio_miedo_pds.setVolume(1.0)
foto_ei_estimulo_excitatorio_miedo_pds = visual.ImageStim(
    win=win,
    name='foto_ei_estimulo_excitatorio_miedo_pds', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# --- Initialize components for Routine "ITI" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
bucle_excitadordetransferencia_pds = data.TrialHandler(nReps=14.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("G"+expInfo['grupo contr']+".xlsx", selection='0:2'),
    seed=None, name='bucle_excitadordetransferencia_pds')
thisExp.addLoop(bucle_excitadordetransferencia_pds)  # add the loop to the experiment
thisBucle_excitadordetransferencia_pd = bucle_excitadordetransferencia_pds.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBucle_excitadordetransferencia_pd.rgb)
if thisBucle_excitadordetransferencia_pd != None:
    for paramName in thisBucle_excitadordetransferencia_pd:
        exec('{} = thisBucle_excitadordetransferencia_pd[paramName]'.format(paramName))

for thisBucle_excitadordetransferencia_pd in bucle_excitadordetransferencia_pds:
    currentLoop = bucle_excitadordetransferencia_pds
    # abbreviate parameter names if possible (e.g. rgb = thisBucle_excitadordetransferencia_pd.rgb)
    if thisBucle_excitadordetransferencia_pd != None:
        for paramName in thisBucle_excitadordetransferencia_pd:
            exec('{} = thisBucle_excitadordetransferencia_pd[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    foto_excitadordetransferencia_pds.setImage(EXCITADOR_DE_TRANSFERENCIA_ADQUISICION)
    EIfotoPERRO_excitadordetransferencia_pds.setImage(EI_FOTO)
    EISONIDO_excitadordetransferencia_pds.setSound(EI_SONIDO, secs=0.7, hamming=True)
    EISONIDO_excitadordetransferencia_pds.setVolume(1.0, log=False)
    # keep track of which components have finished
    ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents = [foto_excitadordetransferencia_pds, EIfotoPERRO_excitadordetransferencia_pds, EISONIDO_excitadordetransferencia_pds]
    for thisComponent in ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
    while continueRoutine and routineTimer.getTime() < 4.8:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *foto_excitadordetransferencia_pds* updates
        if foto_excitadordetransferencia_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foto_excitadordetransferencia_pds.frameNStart = frameN  # exact frame index
            foto_excitadordetransferencia_pds.tStart = t  # local t and not account for scr refresh
            foto_excitadordetransferencia_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_excitadordetransferencia_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_excitadordetransferencia_pds.started')
            foto_excitadordetransferencia_pds.setAutoDraw(True)
        if foto_excitadordetransferencia_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foto_excitadordetransferencia_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                foto_excitadordetransferencia_pds.tStop = t  # not accounting for scr refresh
                foto_excitadordetransferencia_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_excitadordetransferencia_pds.stopped')
                foto_excitadordetransferencia_pds.setAutoDraw(False)
        
        # *EIfotoPERRO_excitadordetransferencia_pds* updates
        if EIfotoPERRO_excitadordetransferencia_pds.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
            # keep track of start time/frame for later
            EIfotoPERRO_excitadordetransferencia_pds.frameNStart = frameN  # exact frame index
            EIfotoPERRO_excitadordetransferencia_pds.tStart = t  # local t and not account for scr refresh
            EIfotoPERRO_excitadordetransferencia_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EIfotoPERRO_excitadordetransferencia_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EIfotoPERRO_excitadordetransferencia_pds.started')
            EIfotoPERRO_excitadordetransferencia_pds.setAutoDraw(True)
        if EIfotoPERRO_excitadordetransferencia_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EIfotoPERRO_excitadordetransferencia_pds.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                EIfotoPERRO_excitadordetransferencia_pds.tStop = t  # not accounting for scr refresh
                EIfotoPERRO_excitadordetransferencia_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EIfotoPERRO_excitadordetransferencia_pds.stopped')
                EIfotoPERRO_excitadordetransferencia_pds.setAutoDraw(False)
        # start/stop EISONIDO_excitadordetransferencia_pds
        if EISONIDO_excitadordetransferencia_pds.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
            # keep track of start time/frame for later
            EISONIDO_excitadordetransferencia_pds.frameNStart = frameN  # exact frame index
            EISONIDO_excitadordetransferencia_pds.tStart = t  # local t and not account for scr refresh
            EISONIDO_excitadordetransferencia_pds.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('EISONIDO_excitadordetransferencia_pds.started', tThisFlipGlobal)
            EISONIDO_excitadordetransferencia_pds.play(when=win)  # sync with win flip
        if EISONIDO_excitadordetransferencia_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > EISONIDO_excitadordetransferencia_pds.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                EISONIDO_excitadordetransferencia_pds.tStop = t  # not accounting for scr refresh
                EISONIDO_excitadordetransferencia_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'EISONIDO_excitadordetransferencia_pds.stopped')
                EISONIDO_excitadordetransferencia_pds.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICION" ---
    for thisComponent in ENTRENAMIENTO_EXCITADOR_DE_TRANSFERENCIA_ADQUISICIONComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    EISONIDO_excitadordetransferencia_pds.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.800000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_iti
    original_color = win.color
    win.color = 'black'  # Cambia el color de fondo negro
    import time
    
    # Inicializar una variable para almacenar el tiempo de inicio del experimento
    inicio_experimento = time.time()
    
    # Crear un objeto de texto para mostrar el tiempo transcurrido
    texto_tiempo = visual.TextStim(win=win, text='', pos=(0, -0.25), height=0.1, color='white')
    
    import random
    
    # Generar una duración aleatoria entre 3 y 5 segundos
    duracion_cross = random.uniform(3, 5)
    
    # Guardar la duración en una variable que puedas utilizar en tu experimento
    thisExp.addData('duracion_cross', duracion_cross)
    # keep track of which components have finished
    ITIComponents = [cross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + duracion_cross-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_iti
    win.color = original_color
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 14.0 repeats of 'bucle_excitadordetransferencia_pds'


# set up handler to look after randomisation of conditions etc
bucle_estimulocompuestoinhibidor_expectativa_PDS = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("G"+expInfo['grupo contr']+".xlsx"),
    seed=None, name='bucle_estimulocompuestoinhibidor_expectativa_PDS')
thisExp.addLoop(bucle_estimulocompuestoinhibidor_expectativa_PDS)  # add the loop to the experiment
thisBucle_estimulocompuestoinhibidor_expectativa_PDS = bucle_estimulocompuestoinhibidor_expectativa_PDS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBucle_estimulocompuestoinhibidor_expectativa_PDS.rgb)
if thisBucle_estimulocompuestoinhibidor_expectativa_PDS != None:
    for paramName in thisBucle_estimulocompuestoinhibidor_expectativa_PDS:
        exec('{} = thisBucle_estimulocompuestoinhibidor_expectativa_PDS[paramName]'.format(paramName))

for thisBucle_estimulocompuestoinhibidor_expectativa_PDS in bucle_estimulocompuestoinhibidor_expectativa_PDS:
    currentLoop = bucle_estimulocompuestoinhibidor_expectativa_PDS
    # abbreviate parameter names if possible (e.g. rgb = thisBucle_estimulocompuestoinhibidor_expectativa_PDS.rgb)
    if thisBucle_estimulocompuestoinhibidor_expectativa_PDS != None:
        for paramName in thisBucle_estimulocompuestoinhibidor_expectativa_PDS:
            exec('{} = thisBucle_estimulocompuestoinhibidor_expectativa_PDS[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ESTIMULO_COMPUESTO_INHIBIDOR_pds" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    foto_inhibidor_a_prueba_pds.setImage(INHIBIDOR_A_PRUEBA_ADQUISICION)
    foto_excitadordetransferencia_pds_foto.setImage(EXCITADOR_DE_TRANSFERENCIA_ADQUISICION)
    escalaexpectativa_estimulocompuestoinhibidor_pds.setText('¿Cuán probable es que se presente la imagen y el sonido desagradable? lala')
    slider_expectativa_estimulocompuestoinhibidor_pds.reset()
    # keep track of which components have finished
    ESTIMULO_COMPUESTO_INHIBIDOR_pdsComponents = [foto_inhibidor_a_prueba_pds, foto_excitadordetransferencia_pds_foto, escalaexpectativa_estimulocompuestoinhibidor_pds, slider_expectativa_estimulocompuestoinhibidor_pds]
    for thisComponent in ESTIMULO_COMPUESTO_INHIBIDOR_pdsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ESTIMULO_COMPUESTO_INHIBIDOR_pds" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *foto_inhibidor_a_prueba_pds* updates
        if foto_inhibidor_a_prueba_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foto_inhibidor_a_prueba_pds.frameNStart = frameN  # exact frame index
            foto_inhibidor_a_prueba_pds.tStart = t  # local t and not account for scr refresh
            foto_inhibidor_a_prueba_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_inhibidor_a_prueba_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_inhibidor_a_prueba_pds.started')
            foto_inhibidor_a_prueba_pds.setAutoDraw(True)
        if foto_inhibidor_a_prueba_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foto_inhibidor_a_prueba_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                foto_inhibidor_a_prueba_pds.tStop = t  # not accounting for scr refresh
                foto_inhibidor_a_prueba_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_inhibidor_a_prueba_pds.stopped')
                foto_inhibidor_a_prueba_pds.setAutoDraw(False)
        
        # *foto_excitadordetransferencia_pds_foto* updates
        if foto_excitadordetransferencia_pds_foto.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foto_excitadordetransferencia_pds_foto.frameNStart = frameN  # exact frame index
            foto_excitadordetransferencia_pds_foto.tStart = t  # local t and not account for scr refresh
            foto_excitadordetransferencia_pds_foto.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_excitadordetransferencia_pds_foto, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_excitadordetransferencia_pds_foto.started')
            foto_excitadordetransferencia_pds_foto.setAutoDraw(True)
        if foto_excitadordetransferencia_pds_foto.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foto_excitadordetransferencia_pds_foto.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                foto_excitadordetransferencia_pds_foto.tStop = t  # not accounting for scr refresh
                foto_excitadordetransferencia_pds_foto.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_excitadordetransferencia_pds_foto.stopped')
                foto_excitadordetransferencia_pds_foto.setAutoDraw(False)
        
        # *escalaexpectativa_estimulocompuestoinhibidor_pds* updates
        if escalaexpectativa_estimulocompuestoinhibidor_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            escalaexpectativa_estimulocompuestoinhibidor_pds.frameNStart = frameN  # exact frame index
            escalaexpectativa_estimulocompuestoinhibidor_pds.tStart = t  # local t and not account for scr refresh
            escalaexpectativa_estimulocompuestoinhibidor_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(escalaexpectativa_estimulocompuestoinhibidor_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'escalaexpectativa_estimulocompuestoinhibidor_pds.started')
            escalaexpectativa_estimulocompuestoinhibidor_pds.setAutoDraw(True)
        if escalaexpectativa_estimulocompuestoinhibidor_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > escalaexpectativa_estimulocompuestoinhibidor_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                escalaexpectativa_estimulocompuestoinhibidor_pds.tStop = t  # not accounting for scr refresh
                escalaexpectativa_estimulocompuestoinhibidor_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'escalaexpectativa_estimulocompuestoinhibidor_pds.stopped')
                escalaexpectativa_estimulocompuestoinhibidor_pds.setAutoDraw(False)
        
        # *slider_expectativa_estimulocompuestoinhibidor_pds* updates
        if slider_expectativa_estimulocompuestoinhibidor_pds.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_expectativa_estimulocompuestoinhibidor_pds.frameNStart = frameN  # exact frame index
            slider_expectativa_estimulocompuestoinhibidor_pds.tStart = t  # local t and not account for scr refresh
            slider_expectativa_estimulocompuestoinhibidor_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_expectativa_estimulocompuestoinhibidor_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_expectativa_estimulocompuestoinhibidor_pds.started')
            slider_expectativa_estimulocompuestoinhibidor_pds.setAutoDraw(True)
        if slider_expectativa_estimulocompuestoinhibidor_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slider_expectativa_estimulocompuestoinhibidor_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                slider_expectativa_estimulocompuestoinhibidor_pds.tStop = t  # not accounting for scr refresh
                slider_expectativa_estimulocompuestoinhibidor_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_expectativa_estimulocompuestoinhibidor_pds.stopped')
                slider_expectativa_estimulocompuestoinhibidor_pds.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ESTIMULO_COMPUESTO_INHIBIDOR_pdsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ESTIMULO_COMPUESTO_INHIBIDOR_pds" ---
    for thisComponent in ESTIMULO_COMPUESTO_INHIBIDOR_pdsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    bucle_estimulocompuestoinhibidor_expectativa_PDS.addData('slider_expectativa_estimulocompuestoinhibidor_pds.response', slider_expectativa_estimulocompuestoinhibidor_pds.getRating())
    bucle_estimulocompuestoinhibidor_expectativa_PDS.addData('slider_expectativa_estimulocompuestoinhibidor_pds.rt', slider_expectativa_estimulocompuestoinhibidor_pds.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_iti
    original_color = win.color
    win.color = 'black'  # Cambia el color de fondo negro
    import time
    
    # Inicializar una variable para almacenar el tiempo de inicio del experimento
    inicio_experimento = time.time()
    
    # Crear un objeto de texto para mostrar el tiempo transcurrido
    texto_tiempo = visual.TextStim(win=win, text='', pos=(0, -0.25), height=0.1, color='white')
    
    import random
    
    # Generar una duración aleatoria entre 3 y 5 segundos
    duracion_cross = random.uniform(3, 5)
    
    # Guardar la duración en una variable que puedas utilizar en tu experimento
    thisExp.addData('duracion_cross', duracion_cross)
    # keep track of which components have finished
    ITIComponents = [cross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + duracion_cross-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_iti
    win.color = original_color
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'bucle_estimulocompuestoinhibidor_expectativa_PDS'


# set up handler to look after randomisation of conditions etc
bucle_estimulocompuestoneutro_expectativa_PDS = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("G"+expInfo['grupo contr']+".xlsx"),
    seed=None, name='bucle_estimulocompuestoneutro_expectativa_PDS')
thisExp.addLoop(bucle_estimulocompuestoneutro_expectativa_PDS)  # add the loop to the experiment
thisBucle_estimulocompuestoneutro_expectativa_PDS = bucle_estimulocompuestoneutro_expectativa_PDS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBucle_estimulocompuestoneutro_expectativa_PDS.rgb)
if thisBucle_estimulocompuestoneutro_expectativa_PDS != None:
    for paramName in thisBucle_estimulocompuestoneutro_expectativa_PDS:
        exec('{} = thisBucle_estimulocompuestoneutro_expectativa_PDS[paramName]'.format(paramName))

for thisBucle_estimulocompuestoneutro_expectativa_PDS in bucle_estimulocompuestoneutro_expectativa_PDS:
    currentLoop = bucle_estimulocompuestoneutro_expectativa_PDS
    # abbreviate parameter names if possible (e.g. rgb = thisBucle_estimulocompuestoneutro_expectativa_PDS.rgb)
    if thisBucle_estimulocompuestoneutro_expectativa_PDS != None:
        for paramName in thisBucle_estimulocompuestoneutro_expectativa_PDS:
            exec('{} = thisBucle_estimulocompuestoneutro_expectativa_PDS[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ESTIMULO_COMPUESTO_NEUTRO_pds" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    foto_estimulo_neutro_pds.setImage(ESTIMULO_NEUTRO_ADQUISICION)
    foto_excitadordetransferencia_estimulocompuestoneutro_pds.setImage(EXCITADOR_DE_TRANSFERENCIA_ADQUISICION)
    escalaexpectativa_estimulocompuestoneutro_pds.setText('¿Cuán probable es que se presente la imagen y el sonido desagradable?')
    slider_estimulocompuestoneutro_pds.reset()
    # keep track of which components have finished
    ESTIMULO_COMPUESTO_NEUTRO_pdsComponents = [foto_estimulo_neutro_pds, foto_excitadordetransferencia_estimulocompuestoneutro_pds, escalaexpectativa_estimulocompuestoneutro_pds, slider_estimulocompuestoneutro_pds]
    for thisComponent in ESTIMULO_COMPUESTO_NEUTRO_pdsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ESTIMULO_COMPUESTO_NEUTRO_pds" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *foto_estimulo_neutro_pds* updates
        if foto_estimulo_neutro_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foto_estimulo_neutro_pds.frameNStart = frameN  # exact frame index
            foto_estimulo_neutro_pds.tStart = t  # local t and not account for scr refresh
            foto_estimulo_neutro_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_estimulo_neutro_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_estimulo_neutro_pds.started')
            foto_estimulo_neutro_pds.setAutoDraw(True)
        if foto_estimulo_neutro_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foto_estimulo_neutro_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                foto_estimulo_neutro_pds.tStop = t  # not accounting for scr refresh
                foto_estimulo_neutro_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_estimulo_neutro_pds.stopped')
                foto_estimulo_neutro_pds.setAutoDraw(False)
        
        # *foto_excitadordetransferencia_estimulocompuestoneutro_pds* updates
        if foto_excitadordetransferencia_estimulocompuestoneutro_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foto_excitadordetransferencia_estimulocompuestoneutro_pds.frameNStart = frameN  # exact frame index
            foto_excitadordetransferencia_estimulocompuestoneutro_pds.tStart = t  # local t and not account for scr refresh
            foto_excitadordetransferencia_estimulocompuestoneutro_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_excitadordetransferencia_estimulocompuestoneutro_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_excitadordetransferencia_estimulocompuestoneutro_pds.started')
            foto_excitadordetransferencia_estimulocompuestoneutro_pds.setAutoDraw(True)
        if foto_excitadordetransferencia_estimulocompuestoneutro_pds.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                foto_excitadordetransferencia_estimulocompuestoneutro_pds.tStop = t  # not accounting for scr refresh
                foto_excitadordetransferencia_estimulocompuestoneutro_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_excitadordetransferencia_estimulocompuestoneutro_pds.stopped')
                foto_excitadordetransferencia_estimulocompuestoneutro_pds.setAutoDraw(False)
        
        # *escalaexpectativa_estimulocompuestoneutro_pds* updates
        if escalaexpectativa_estimulocompuestoneutro_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            escalaexpectativa_estimulocompuestoneutro_pds.frameNStart = frameN  # exact frame index
            escalaexpectativa_estimulocompuestoneutro_pds.tStart = t  # local t and not account for scr refresh
            escalaexpectativa_estimulocompuestoneutro_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(escalaexpectativa_estimulocompuestoneutro_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'escalaexpectativa_estimulocompuestoneutro_pds.started')
            escalaexpectativa_estimulocompuestoneutro_pds.setAutoDraw(True)
        if escalaexpectativa_estimulocompuestoneutro_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > escalaexpectativa_estimulocompuestoneutro_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                escalaexpectativa_estimulocompuestoneutro_pds.tStop = t  # not accounting for scr refresh
                escalaexpectativa_estimulocompuestoneutro_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'escalaexpectativa_estimulocompuestoneutro_pds.stopped')
                escalaexpectativa_estimulocompuestoneutro_pds.setAutoDraw(False)
        
        # *slider_estimulocompuestoneutro_pds* updates
        if slider_estimulocompuestoneutro_pds.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_estimulocompuestoneutro_pds.frameNStart = frameN  # exact frame index
            slider_estimulocompuestoneutro_pds.tStart = t  # local t and not account for scr refresh
            slider_estimulocompuestoneutro_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_estimulocompuestoneutro_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_estimulocompuestoneutro_pds.started')
            slider_estimulocompuestoneutro_pds.setAutoDraw(True)
        if slider_estimulocompuestoneutro_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slider_estimulocompuestoneutro_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                slider_estimulocompuestoneutro_pds.tStop = t  # not accounting for scr refresh
                slider_estimulocompuestoneutro_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_estimulocompuestoneutro_pds.stopped')
                slider_estimulocompuestoneutro_pds.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ESTIMULO_COMPUESTO_NEUTRO_pdsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ESTIMULO_COMPUESTO_NEUTRO_pds" ---
    for thisComponent in ESTIMULO_COMPUESTO_NEUTRO_pdsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    bucle_estimulocompuestoneutro_expectativa_PDS.addData('slider_estimulocompuestoneutro_pds.response', slider_estimulocompuestoneutro_pds.getRating())
    bucle_estimulocompuestoneutro_expectativa_PDS.addData('slider_estimulocompuestoneutro_pds.rt', slider_estimulocompuestoneutro_pds.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_iti
    original_color = win.color
    win.color = 'black'  # Cambia el color de fondo negro
    import time
    
    # Inicializar una variable para almacenar el tiempo de inicio del experimento
    inicio_experimento = time.time()
    
    # Crear un objeto de texto para mostrar el tiempo transcurrido
    texto_tiempo = visual.TextStim(win=win, text='', pos=(0, -0.25), height=0.1, color='white')
    
    import random
    
    # Generar una duración aleatoria entre 3 y 5 segundos
    duracion_cross = random.uniform(3, 5)
    
    # Guardar la duración en una variable que puedas utilizar en tu experimento
    thisExp.addData('duracion_cross', duracion_cross)
    # keep track of which components have finished
    ITIComponents = [cross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + duracion_cross-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_iti
    win.color = original_color
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'bucle_estimulocompuestoneutro_expectativa_PDS'


# set up handler to look after randomisation of conditions etc
bucle_estimuloexcitatorio_expectativa_PDS = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("G"+expInfo['grupo contr']+".xlsx", selection='0:2'),
    seed=None, name='bucle_estimuloexcitatorio_expectativa_PDS')
thisExp.addLoop(bucle_estimuloexcitatorio_expectativa_PDS)  # add the loop to the experiment
thisBucle_estimuloexcitatorio_expectativa_PDS = bucle_estimuloexcitatorio_expectativa_PDS.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBucle_estimuloexcitatorio_expectativa_PDS.rgb)
if thisBucle_estimuloexcitatorio_expectativa_PDS != None:
    for paramName in thisBucle_estimuloexcitatorio_expectativa_PDS:
        exec('{} = thisBucle_estimuloexcitatorio_expectativa_PDS[paramName]'.format(paramName))

for thisBucle_estimuloexcitatorio_expectativa_PDS in bucle_estimuloexcitatorio_expectativa_PDS:
    currentLoop = bucle_estimuloexcitatorio_expectativa_PDS
    # abbreviate parameter names if possible (e.g. rgb = thisBucle_estimuloexcitatorio_expectativa_PDS.rgb)
    if thisBucle_estimuloexcitatorio_expectativa_PDS != None:
        for paramName in thisBucle_estimuloexcitatorio_expectativa_PDS:
            exec('{} = thisBucle_estimuloexcitatorio_expectativa_PDS[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ESTIMULO_EXCITATORIO_PDS" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    foto_estimulo_condicionado_excitatorio_pds.setImage(ESTIMULO_EXCITATORIO)
    escalaexpectativa_estimulocondicionadoexcitatorio_pds.setText('¿Cuán probable es que se presente la imagen y el sonido desagradable?')
    slider_estimulocondicionadoexcitatorio_pds.reset()
    eifoto_estimulocondicionadoexcitatorio_pds.setImage(EI_FOTO)
    eisonido_estimulocondicionadoexcitatorio_pds.setSound(EI_SONIDO, secs=0.7, hamming=True)
    eisonido_estimulocondicionadoexcitatorio_pds.setVolume(1.0, log=False)
    # keep track of which components have finished
    ESTIMULO_EXCITATORIO_PDSComponents = [foto_estimulo_condicionado_excitatorio_pds, escalaexpectativa_estimulocondicionadoexcitatorio_pds, slider_estimulocondicionadoexcitatorio_pds, eifoto_estimulocondicionadoexcitatorio_pds, eisonido_estimulocondicionadoexcitatorio_pds]
    for thisComponent in ESTIMULO_EXCITATORIO_PDSComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ESTIMULO_EXCITATORIO_PDS" ---
    while continueRoutine and routineTimer.getTime() < 4.8:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *foto_estimulo_condicionado_excitatorio_pds* updates
        if foto_estimulo_condicionado_excitatorio_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foto_estimulo_condicionado_excitatorio_pds.frameNStart = frameN  # exact frame index
            foto_estimulo_condicionado_excitatorio_pds.tStart = t  # local t and not account for scr refresh
            foto_estimulo_condicionado_excitatorio_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_estimulo_condicionado_excitatorio_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_estimulo_condicionado_excitatorio_pds.started')
            foto_estimulo_condicionado_excitatorio_pds.setAutoDraw(True)
        if foto_estimulo_condicionado_excitatorio_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foto_estimulo_condicionado_excitatorio_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                foto_estimulo_condicionado_excitatorio_pds.tStop = t  # not accounting for scr refresh
                foto_estimulo_condicionado_excitatorio_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_estimulo_condicionado_excitatorio_pds.stopped')
                foto_estimulo_condicionado_excitatorio_pds.setAutoDraw(False)
        
        # *escalaexpectativa_estimulocondicionadoexcitatorio_pds* updates
        if escalaexpectativa_estimulocondicionadoexcitatorio_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            escalaexpectativa_estimulocondicionadoexcitatorio_pds.frameNStart = frameN  # exact frame index
            escalaexpectativa_estimulocondicionadoexcitatorio_pds.tStart = t  # local t and not account for scr refresh
            escalaexpectativa_estimulocondicionadoexcitatorio_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(escalaexpectativa_estimulocondicionadoexcitatorio_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'escalaexpectativa_estimulocondicionadoexcitatorio_pds.started')
            escalaexpectativa_estimulocondicionadoexcitatorio_pds.setAutoDraw(True)
        if escalaexpectativa_estimulocondicionadoexcitatorio_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > escalaexpectativa_estimulocondicionadoexcitatorio_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                escalaexpectativa_estimulocondicionadoexcitatorio_pds.tStop = t  # not accounting for scr refresh
                escalaexpectativa_estimulocondicionadoexcitatorio_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'escalaexpectativa_estimulocondicionadoexcitatorio_pds.stopped')
                escalaexpectativa_estimulocondicionadoexcitatorio_pds.setAutoDraw(False)
        
        # *slider_estimulocondicionadoexcitatorio_pds* updates
        if slider_estimulocondicionadoexcitatorio_pds.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            slider_estimulocondicionadoexcitatorio_pds.frameNStart = frameN  # exact frame index
            slider_estimulocondicionadoexcitatorio_pds.tStart = t  # local t and not account for scr refresh
            slider_estimulocondicionadoexcitatorio_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_estimulocondicionadoexcitatorio_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_estimulocondicionadoexcitatorio_pds.started')
            slider_estimulocondicionadoexcitatorio_pds.setAutoDraw(True)
        if slider_estimulocondicionadoexcitatorio_pds.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                slider_estimulocondicionadoexcitatorio_pds.tStop = t  # not accounting for scr refresh
                slider_estimulocondicionadoexcitatorio_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_estimulocondicionadoexcitatorio_pds.stopped')
                slider_estimulocondicionadoexcitatorio_pds.setAutoDraw(False)
        
        # *eifoto_estimulocondicionadoexcitatorio_pds* updates
        if eifoto_estimulocondicionadoexcitatorio_pds.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
            # keep track of start time/frame for later
            eifoto_estimulocondicionadoexcitatorio_pds.frameNStart = frameN  # exact frame index
            eifoto_estimulocondicionadoexcitatorio_pds.tStart = t  # local t and not account for scr refresh
            eifoto_estimulocondicionadoexcitatorio_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(eifoto_estimulocondicionadoexcitatorio_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'eifoto_estimulocondicionadoexcitatorio_pds.started')
            eifoto_estimulocondicionadoexcitatorio_pds.setAutoDraw(True)
        if eifoto_estimulocondicionadoexcitatorio_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eifoto_estimulocondicionadoexcitatorio_pds.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                eifoto_estimulocondicionadoexcitatorio_pds.tStop = t  # not accounting for scr refresh
                eifoto_estimulocondicionadoexcitatorio_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eifoto_estimulocondicionadoexcitatorio_pds.stopped')
                eifoto_estimulocondicionadoexcitatorio_pds.setAutoDraw(False)
        # start/stop eisonido_estimulocondicionadoexcitatorio_pds
        if eisonido_estimulocondicionadoexcitatorio_pds.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
            # keep track of start time/frame for later
            eisonido_estimulocondicionadoexcitatorio_pds.frameNStart = frameN  # exact frame index
            eisonido_estimulocondicionadoexcitatorio_pds.tStart = t  # local t and not account for scr refresh
            eisonido_estimulocondicionadoexcitatorio_pds.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('eisonido_estimulocondicionadoexcitatorio_pds.started', tThisFlipGlobal)
            eisonido_estimulocondicionadoexcitatorio_pds.play(when=win)  # sync with win flip
        if eisonido_estimulocondicionadoexcitatorio_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > eisonido_estimulocondicionadoexcitatorio_pds.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                eisonido_estimulocondicionadoexcitatorio_pds.tStop = t  # not accounting for scr refresh
                eisonido_estimulocondicionadoexcitatorio_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'eisonido_estimulocondicionadoexcitatorio_pds.stopped')
                eisonido_estimulocondicionadoexcitatorio_pds.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ESTIMULO_EXCITATORIO_PDSComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ESTIMULO_EXCITATORIO_PDS" ---
    for thisComponent in ESTIMULO_EXCITATORIO_PDSComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    bucle_estimuloexcitatorio_expectativa_PDS.addData('slider_estimulocondicionadoexcitatorio_pds.response', slider_estimulocondicionadoexcitatorio_pds.getRating())
    bucle_estimuloexcitatorio_expectativa_PDS.addData('slider_estimulocondicionadoexcitatorio_pds.rt', slider_estimulocondicionadoexcitatorio_pds.getRT())
    eisonido_estimulocondicionadoexcitatorio_pds.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.800000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_iti
    original_color = win.color
    win.color = 'black'  # Cambia el color de fondo negro
    import time
    
    # Inicializar una variable para almacenar el tiempo de inicio del experimento
    inicio_experimento = time.time()
    
    # Crear un objeto de texto para mostrar el tiempo transcurrido
    texto_tiempo = visual.TextStim(win=win, text='', pos=(0, -0.25), height=0.1, color='white')
    
    import random
    
    # Generar una duración aleatoria entre 3 y 5 segundos
    duracion_cross = random.uniform(3, 5)
    
    # Guardar la duración en una variable que puedas utilizar en tu experimento
    thisExp.addData('duracion_cross', duracion_cross)
    # keep track of which components have finished
    ITIComponents = [cross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + duracion_cross-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_iti
    win.color = original_color
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'bucle_estimuloexcitatorio_expectativa_PDS'


# set up handler to look after randomisation of conditions etc
bucle_estimulocompuestoinhibidor_miedo_pds = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("G"+expInfo['grupo contr']+".xlsx"),
    seed=None, name='bucle_estimulocompuestoinhibidor_miedo_pds')
thisExp.addLoop(bucle_estimulocompuestoinhibidor_miedo_pds)  # add the loop to the experiment
thisBucle_estimulocompuestoinhibidor_miedo_pd = bucle_estimulocompuestoinhibidor_miedo_pds.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBucle_estimulocompuestoinhibidor_miedo_pd.rgb)
if thisBucle_estimulocompuestoinhibidor_miedo_pd != None:
    for paramName in thisBucle_estimulocompuestoinhibidor_miedo_pd:
        exec('{} = thisBucle_estimulocompuestoinhibidor_miedo_pd[paramName]'.format(paramName))

for thisBucle_estimulocompuestoinhibidor_miedo_pd in bucle_estimulocompuestoinhibidor_miedo_pds:
    currentLoop = bucle_estimulocompuestoinhibidor_miedo_pds
    # abbreviate parameter names if possible (e.g. rgb = thisBucle_estimulocompuestoinhibidor_miedo_pd.rgb)
    if thisBucle_estimulocompuestoinhibidor_miedo_pd != None:
        for paramName in thisBucle_estimulocompuestoinhibidor_miedo_pd:
            exec('{} = thisBucle_estimulocompuestoinhibidor_miedo_pd[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "estimulo_compuesto_inhibidor_miedo_pds" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    foto_inhibidor_a_prueba_miedo_pds.setImage(INHIBIDOR_A_PRUEBA_ADQUISICION)
    foto_excitador_de_transferencia_miedo_pds.setImage(EXCITADOR_DE_TRANSFERENCIA_ADQUISICION)
    texto_escala_miedo_estimulo_compuesto_inhibidor_pds.setText('¿Cuánto miedo te da esta foto?')
    slider_miedo_estimulo_compuesto_inhibidor_pds.reset()
    # keep track of which components have finished
    estimulo_compuesto_inhibidor_miedo_pdsComponents = [foto_inhibidor_a_prueba_miedo_pds, foto_excitador_de_transferencia_miedo_pds, texto_escala_miedo_estimulo_compuesto_inhibidor_pds, slider_miedo_estimulo_compuesto_inhibidor_pds]
    for thisComponent in estimulo_compuesto_inhibidor_miedo_pdsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "estimulo_compuesto_inhibidor_miedo_pds" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *foto_inhibidor_a_prueba_miedo_pds* updates
        if foto_inhibidor_a_prueba_miedo_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foto_inhibidor_a_prueba_miedo_pds.frameNStart = frameN  # exact frame index
            foto_inhibidor_a_prueba_miedo_pds.tStart = t  # local t and not account for scr refresh
            foto_inhibidor_a_prueba_miedo_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_inhibidor_a_prueba_miedo_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_inhibidor_a_prueba_miedo_pds.started')
            foto_inhibidor_a_prueba_miedo_pds.setAutoDraw(True)
        if foto_inhibidor_a_prueba_miedo_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foto_inhibidor_a_prueba_miedo_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                foto_inhibidor_a_prueba_miedo_pds.tStop = t  # not accounting for scr refresh
                foto_inhibidor_a_prueba_miedo_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_inhibidor_a_prueba_miedo_pds.stopped')
                foto_inhibidor_a_prueba_miedo_pds.setAutoDraw(False)
        
        # *foto_excitador_de_transferencia_miedo_pds* updates
        if foto_excitador_de_transferencia_miedo_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foto_excitador_de_transferencia_miedo_pds.frameNStart = frameN  # exact frame index
            foto_excitador_de_transferencia_miedo_pds.tStart = t  # local t and not account for scr refresh
            foto_excitador_de_transferencia_miedo_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_excitador_de_transferencia_miedo_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_excitador_de_transferencia_miedo_pds.started')
            foto_excitador_de_transferencia_miedo_pds.setAutoDraw(True)
        if foto_excitador_de_transferencia_miedo_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foto_excitador_de_transferencia_miedo_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                foto_excitador_de_transferencia_miedo_pds.tStop = t  # not accounting for scr refresh
                foto_excitador_de_transferencia_miedo_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_excitador_de_transferencia_miedo_pds.stopped')
                foto_excitador_de_transferencia_miedo_pds.setAutoDraw(False)
        
        # *texto_escala_miedo_estimulo_compuesto_inhibidor_pds* updates
        if texto_escala_miedo_estimulo_compuesto_inhibidor_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            texto_escala_miedo_estimulo_compuesto_inhibidor_pds.frameNStart = frameN  # exact frame index
            texto_escala_miedo_estimulo_compuesto_inhibidor_pds.tStart = t  # local t and not account for scr refresh
            texto_escala_miedo_estimulo_compuesto_inhibidor_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(texto_escala_miedo_estimulo_compuesto_inhibidor_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'texto_escala_miedo_estimulo_compuesto_inhibidor_pds.started')
            texto_escala_miedo_estimulo_compuesto_inhibidor_pds.setAutoDraw(True)
        if texto_escala_miedo_estimulo_compuesto_inhibidor_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > texto_escala_miedo_estimulo_compuesto_inhibidor_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                texto_escala_miedo_estimulo_compuesto_inhibidor_pds.tStop = t  # not accounting for scr refresh
                texto_escala_miedo_estimulo_compuesto_inhibidor_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'texto_escala_miedo_estimulo_compuesto_inhibidor_pds.stopped')
                texto_escala_miedo_estimulo_compuesto_inhibidor_pds.setAutoDraw(False)
        
        # *slider_miedo_estimulo_compuesto_inhibidor_pds* updates
        if slider_miedo_estimulo_compuesto_inhibidor_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_miedo_estimulo_compuesto_inhibidor_pds.frameNStart = frameN  # exact frame index
            slider_miedo_estimulo_compuesto_inhibidor_pds.tStart = t  # local t and not account for scr refresh
            slider_miedo_estimulo_compuesto_inhibidor_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_miedo_estimulo_compuesto_inhibidor_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_miedo_estimulo_compuesto_inhibidor_pds.started')
            slider_miedo_estimulo_compuesto_inhibidor_pds.setAutoDraw(True)
        if slider_miedo_estimulo_compuesto_inhibidor_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slider_miedo_estimulo_compuesto_inhibidor_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                slider_miedo_estimulo_compuesto_inhibidor_pds.tStop = t  # not accounting for scr refresh
                slider_miedo_estimulo_compuesto_inhibidor_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_miedo_estimulo_compuesto_inhibidor_pds.stopped')
                slider_miedo_estimulo_compuesto_inhibidor_pds.setAutoDraw(False)
        
        # Check slider_miedo_estimulo_compuesto_inhibidor_pds for response to end routine
        if slider_miedo_estimulo_compuesto_inhibidor_pds.getRating() is not None and slider_miedo_estimulo_compuesto_inhibidor_pds.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in estimulo_compuesto_inhibidor_miedo_pdsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "estimulo_compuesto_inhibidor_miedo_pds" ---
    for thisComponent in estimulo_compuesto_inhibidor_miedo_pdsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    bucle_estimulocompuestoinhibidor_miedo_pds.addData('slider_miedo_estimulo_compuesto_inhibidor_pds.response', slider_miedo_estimulo_compuesto_inhibidor_pds.getRating())
    bucle_estimulocompuestoinhibidor_miedo_pds.addData('slider_miedo_estimulo_compuesto_inhibidor_pds.rt', slider_miedo_estimulo_compuesto_inhibidor_pds.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_iti
    original_color = win.color
    win.color = 'black'  # Cambia el color de fondo negro
    import time
    
    # Inicializar una variable para almacenar el tiempo de inicio del experimento
    inicio_experimento = time.time()
    
    # Crear un objeto de texto para mostrar el tiempo transcurrido
    texto_tiempo = visual.TextStim(win=win, text='', pos=(0, -0.25), height=0.1, color='white')
    
    import random
    
    # Generar una duración aleatoria entre 3 y 5 segundos
    duracion_cross = random.uniform(3, 5)
    
    # Guardar la duración en una variable que puedas utilizar en tu experimento
    thisExp.addData('duracion_cross', duracion_cross)
    # keep track of which components have finished
    ITIComponents = [cross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + duracion_cross-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_iti
    win.color = original_color
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'bucle_estimulocompuestoinhibidor_miedo_pds'


# set up handler to look after randomisation of conditions etc
bucle_estimulocompuestoneutro_miedo_pds = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("G"+expInfo['grupo contr']+".xlsx"),
    seed=None, name='bucle_estimulocompuestoneutro_miedo_pds')
thisExp.addLoop(bucle_estimulocompuestoneutro_miedo_pds)  # add the loop to the experiment
thisBucle_estimulocompuestoneutro_miedo_pd = bucle_estimulocompuestoneutro_miedo_pds.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBucle_estimulocompuestoneutro_miedo_pd.rgb)
if thisBucle_estimulocompuestoneutro_miedo_pd != None:
    for paramName in thisBucle_estimulocompuestoneutro_miedo_pd:
        exec('{} = thisBucle_estimulocompuestoneutro_miedo_pd[paramName]'.format(paramName))

for thisBucle_estimulocompuestoneutro_miedo_pd in bucle_estimulocompuestoneutro_miedo_pds:
    currentLoop = bucle_estimulocompuestoneutro_miedo_pds
    # abbreviate parameter names if possible (e.g. rgb = thisBucle_estimulocompuestoneutro_miedo_pd.rgb)
    if thisBucle_estimulocompuestoneutro_miedo_pd != None:
        for paramName in thisBucle_estimulocompuestoneutro_miedo_pd:
            exec('{} = thisBucle_estimulocompuestoneutro_miedo_pd[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "estimulo_compuesto_neutro_miedo_pds" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    foto_estimulo_compuesto_neutro_miedo_pds.setImage(ESTIMULO_NEUTRO_ADQUISICION)
    foto_excitador_transferencia_miedo_pds.setImage(EXCITADOR_DE_TRANSFERENCIA_ADQUISICION)
    texto_estimulo_compuesto_neutro_miedo_pds.setText('¿Cuánto miedo te da esta foto?')
    slider_.reset()
    # keep track of which components have finished
    estimulo_compuesto_neutro_miedo_pdsComponents = [foto_estimulo_compuesto_neutro_miedo_pds, foto_excitador_transferencia_miedo_pds, texto_estimulo_compuesto_neutro_miedo_pds, slider_]
    for thisComponent in estimulo_compuesto_neutro_miedo_pdsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "estimulo_compuesto_neutro_miedo_pds" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *foto_estimulo_compuesto_neutro_miedo_pds* updates
        if foto_estimulo_compuesto_neutro_miedo_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foto_estimulo_compuesto_neutro_miedo_pds.frameNStart = frameN  # exact frame index
            foto_estimulo_compuesto_neutro_miedo_pds.tStart = t  # local t and not account for scr refresh
            foto_estimulo_compuesto_neutro_miedo_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_estimulo_compuesto_neutro_miedo_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_estimulo_compuesto_neutro_miedo_pds.started')
            foto_estimulo_compuesto_neutro_miedo_pds.setAutoDraw(True)
        if foto_estimulo_compuesto_neutro_miedo_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foto_estimulo_compuesto_neutro_miedo_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                foto_estimulo_compuesto_neutro_miedo_pds.tStop = t  # not accounting for scr refresh
                foto_estimulo_compuesto_neutro_miedo_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_estimulo_compuesto_neutro_miedo_pds.stopped')
                foto_estimulo_compuesto_neutro_miedo_pds.setAutoDraw(False)
        
        # *foto_excitador_transferencia_miedo_pds* updates
        if foto_excitador_transferencia_miedo_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foto_excitador_transferencia_miedo_pds.frameNStart = frameN  # exact frame index
            foto_excitador_transferencia_miedo_pds.tStart = t  # local t and not account for scr refresh
            foto_excitador_transferencia_miedo_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_excitador_transferencia_miedo_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_excitador_transferencia_miedo_pds.started')
            foto_excitador_transferencia_miedo_pds.setAutoDraw(True)
        if foto_excitador_transferencia_miedo_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foto_excitador_transferencia_miedo_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                foto_excitador_transferencia_miedo_pds.tStop = t  # not accounting for scr refresh
                foto_excitador_transferencia_miedo_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_excitador_transferencia_miedo_pds.stopped')
                foto_excitador_transferencia_miedo_pds.setAutoDraw(False)
        
        # *texto_estimulo_compuesto_neutro_miedo_pds* updates
        if texto_estimulo_compuesto_neutro_miedo_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            texto_estimulo_compuesto_neutro_miedo_pds.frameNStart = frameN  # exact frame index
            texto_estimulo_compuesto_neutro_miedo_pds.tStart = t  # local t and not account for scr refresh
            texto_estimulo_compuesto_neutro_miedo_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(texto_estimulo_compuesto_neutro_miedo_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'texto_estimulo_compuesto_neutro_miedo_pds.started')
            texto_estimulo_compuesto_neutro_miedo_pds.setAutoDraw(True)
        if texto_estimulo_compuesto_neutro_miedo_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > texto_estimulo_compuesto_neutro_miedo_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                texto_estimulo_compuesto_neutro_miedo_pds.tStop = t  # not accounting for scr refresh
                texto_estimulo_compuesto_neutro_miedo_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'texto_estimulo_compuesto_neutro_miedo_pds.stopped')
                texto_estimulo_compuesto_neutro_miedo_pds.setAutoDraw(False)
        
        # *slider_* updates
        if slider_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_.frameNStart = frameN  # exact frame index
            slider_.tStart = t  # local t and not account for scr refresh
            slider_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_.started')
            slider_.setAutoDraw(True)
        if slider_.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slider_.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                slider_.tStop = t  # not accounting for scr refresh
                slider_.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_.stopped')
                slider_.setAutoDraw(False)
        
        # Check slider_ for response to end routine
        if slider_.getRating() is not None and slider_.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in estimulo_compuesto_neutro_miedo_pdsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "estimulo_compuesto_neutro_miedo_pds" ---
    for thisComponent in estimulo_compuesto_neutro_miedo_pdsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    bucle_estimulocompuestoneutro_miedo_pds.addData('slider_.response', slider_.getRating())
    bucle_estimulocompuestoneutro_miedo_pds.addData('slider_.rt', slider_.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_iti
    original_color = win.color
    win.color = 'black'  # Cambia el color de fondo negro
    import time
    
    # Inicializar una variable para almacenar el tiempo de inicio del experimento
    inicio_experimento = time.time()
    
    # Crear un objeto de texto para mostrar el tiempo transcurrido
    texto_tiempo = visual.TextStim(win=win, text='', pos=(0, -0.25), height=0.1, color='white')
    
    import random
    
    # Generar una duración aleatoria entre 3 y 5 segundos
    duracion_cross = random.uniform(3, 5)
    
    # Guardar la duración en una variable que puedas utilizar en tu experimento
    thisExp.addData('duracion_cross', duracion_cross)
    # keep track of which components have finished
    ITIComponents = [cross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + duracion_cross-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_iti
    win.color = original_color
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'bucle_estimulocompuestoneutro_miedo_pds'


# set up handler to look after randomisation of conditions etc
bucle_estimuloexcitatorio_miedo_pds = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("G"+expInfo['grupo contr']+".xlsx"),
    seed=0:2, name='bucle_estimuloexcitatorio_miedo_pds')
thisExp.addLoop(bucle_estimuloexcitatorio_miedo_pds)  # add the loop to the experiment
thisBucle_estimuloexcitatorio_miedo_pd = bucle_estimuloexcitatorio_miedo_pds.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBucle_estimuloexcitatorio_miedo_pd.rgb)
if thisBucle_estimuloexcitatorio_miedo_pd != None:
    for paramName in thisBucle_estimuloexcitatorio_miedo_pd:
        exec('{} = thisBucle_estimuloexcitatorio_miedo_pd[paramName]'.format(paramName))

for thisBucle_estimuloexcitatorio_miedo_pd in bucle_estimuloexcitatorio_miedo_pds:
    currentLoop = bucle_estimuloexcitatorio_miedo_pds
    # abbreviate parameter names if possible (e.g. rgb = thisBucle_estimuloexcitatorio_miedo_pd.rgb)
    if thisBucle_estimuloexcitatorio_miedo_pd != None:
        for paramName in thisBucle_estimuloexcitatorio_miedo_pd:
            exec('{} = thisBucle_estimuloexcitatorio_miedo_pd[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "estimulo_excitatorio_miedo_pds" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    foto_estimulo_excitatorio_miedo_pds.setImage(ESTIMULO_EXCITATORIO)
    texto_estimulo_excitatorio_miedo_pds.setText('¿Cuánto miedo tienes?')
    slider_estimulo_condicionado_excitatorio_miedo_pds.reset()
    sonido_ei_estimulo_excitatorio_miedo_pds.setSound(EI_SONIDO, secs=0.7, hamming=True)
    sonido_ei_estimulo_excitatorio_miedo_pds.setVolume(1.0, log=False)
    foto_ei_estimulo_excitatorio_miedo_pds.setImage(EI_SONIDO)
    # keep track of which components have finished
    estimulo_excitatorio_miedo_pdsComponents = [foto_estimulo_excitatorio_miedo_pds, texto_estimulo_excitatorio_miedo_pds, slider_estimulo_condicionado_excitatorio_miedo_pds, sonido_ei_estimulo_excitatorio_miedo_pds, foto_ei_estimulo_excitatorio_miedo_pds]
    for thisComponent in estimulo_excitatorio_miedo_pdsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "estimulo_excitatorio_miedo_pds" ---
    while continueRoutine and routineTimer.getTime() < 4.8:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *foto_estimulo_excitatorio_miedo_pds* updates
        if foto_estimulo_excitatorio_miedo_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foto_estimulo_excitatorio_miedo_pds.frameNStart = frameN  # exact frame index
            foto_estimulo_excitatorio_miedo_pds.tStart = t  # local t and not account for scr refresh
            foto_estimulo_excitatorio_miedo_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_estimulo_excitatorio_miedo_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_estimulo_excitatorio_miedo_pds.started')
            foto_estimulo_excitatorio_miedo_pds.setAutoDraw(True)
        if foto_estimulo_excitatorio_miedo_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foto_estimulo_excitatorio_miedo_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                foto_estimulo_excitatorio_miedo_pds.tStop = t  # not accounting for scr refresh
                foto_estimulo_excitatorio_miedo_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_estimulo_excitatorio_miedo_pds.stopped')
                foto_estimulo_excitatorio_miedo_pds.setAutoDraw(False)
        
        # *texto_estimulo_excitatorio_miedo_pds* updates
        if texto_estimulo_excitatorio_miedo_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            texto_estimulo_excitatorio_miedo_pds.frameNStart = frameN  # exact frame index
            texto_estimulo_excitatorio_miedo_pds.tStart = t  # local t and not account for scr refresh
            texto_estimulo_excitatorio_miedo_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(texto_estimulo_excitatorio_miedo_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'texto_estimulo_excitatorio_miedo_pds.started')
            texto_estimulo_excitatorio_miedo_pds.setAutoDraw(True)
        if texto_estimulo_excitatorio_miedo_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > texto_estimulo_excitatorio_miedo_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                texto_estimulo_excitatorio_miedo_pds.tStop = t  # not accounting for scr refresh
                texto_estimulo_excitatorio_miedo_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'texto_estimulo_excitatorio_miedo_pds.stopped')
                texto_estimulo_excitatorio_miedo_pds.setAutoDraw(False)
        
        # *slider_estimulo_condicionado_excitatorio_miedo_pds* updates
        if slider_estimulo_condicionado_excitatorio_miedo_pds.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_estimulo_condicionado_excitatorio_miedo_pds.frameNStart = frameN  # exact frame index
            slider_estimulo_condicionado_excitatorio_miedo_pds.tStart = t  # local t and not account for scr refresh
            slider_estimulo_condicionado_excitatorio_miedo_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_estimulo_condicionado_excitatorio_miedo_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_estimulo_condicionado_excitatorio_miedo_pds.started')
            slider_estimulo_condicionado_excitatorio_miedo_pds.setAutoDraw(True)
        if slider_estimulo_condicionado_excitatorio_miedo_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > slider_estimulo_condicionado_excitatorio_miedo_pds.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                slider_estimulo_condicionado_excitatorio_miedo_pds.tStop = t  # not accounting for scr refresh
                slider_estimulo_condicionado_excitatorio_miedo_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_estimulo_condicionado_excitatorio_miedo_pds.stopped')
                slider_estimulo_condicionado_excitatorio_miedo_pds.setAutoDraw(False)
        # start/stop sonido_ei_estimulo_excitatorio_miedo_pds
        if sonido_ei_estimulo_excitatorio_miedo_pds.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
            # keep track of start time/frame for later
            sonido_ei_estimulo_excitatorio_miedo_pds.frameNStart = frameN  # exact frame index
            sonido_ei_estimulo_excitatorio_miedo_pds.tStart = t  # local t and not account for scr refresh
            sonido_ei_estimulo_excitatorio_miedo_pds.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sonido_ei_estimulo_excitatorio_miedo_pds.started', tThisFlipGlobal)
            sonido_ei_estimulo_excitatorio_miedo_pds.play(when=win)  # sync with win flip
        if sonido_ei_estimulo_excitatorio_miedo_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sonido_ei_estimulo_excitatorio_miedo_pds.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                sonido_ei_estimulo_excitatorio_miedo_pds.tStop = t  # not accounting for scr refresh
                sonido_ei_estimulo_excitatorio_miedo_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sonido_ei_estimulo_excitatorio_miedo_pds.stopped')
                sonido_ei_estimulo_excitatorio_miedo_pds.stop()
        
        # *foto_ei_estimulo_excitatorio_miedo_pds* updates
        if foto_ei_estimulo_excitatorio_miedo_pds.status == NOT_STARTED and tThisFlip >= 4.1-frameTolerance:
            # keep track of start time/frame for later
            foto_ei_estimulo_excitatorio_miedo_pds.frameNStart = frameN  # exact frame index
            foto_ei_estimulo_excitatorio_miedo_pds.tStart = t  # local t and not account for scr refresh
            foto_ei_estimulo_excitatorio_miedo_pds.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foto_ei_estimulo_excitatorio_miedo_pds, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'foto_ei_estimulo_excitatorio_miedo_pds.started')
            foto_ei_estimulo_excitatorio_miedo_pds.setAutoDraw(True)
        if foto_ei_estimulo_excitatorio_miedo_pds.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > foto_ei_estimulo_excitatorio_miedo_pds.tStartRefresh + 0.7-frameTolerance:
                # keep track of stop time/frame for later
                foto_ei_estimulo_excitatorio_miedo_pds.tStop = t  # not accounting for scr refresh
                foto_ei_estimulo_excitatorio_miedo_pds.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'foto_ei_estimulo_excitatorio_miedo_pds.stopped')
                foto_ei_estimulo_excitatorio_miedo_pds.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in estimulo_excitatorio_miedo_pdsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "estimulo_excitatorio_miedo_pds" ---
    for thisComponent in estimulo_excitatorio_miedo_pdsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    bucle_estimuloexcitatorio_miedo_pds.addData('slider_estimulo_condicionado_excitatorio_miedo_pds.response', slider_estimulo_condicionado_excitatorio_miedo_pds.getRating())
    bucle_estimuloexcitatorio_miedo_pds.addData('slider_estimulo_condicionado_excitatorio_miedo_pds.rt', slider_estimulo_condicionado_excitatorio_miedo_pds.getRT())
    sonido_ei_estimulo_excitatorio_miedo_pds.stop()  # ensure sound has stopped at end of routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.800000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_iti
    original_color = win.color
    win.color = 'black'  # Cambia el color de fondo negro
    import time
    
    # Inicializar una variable para almacenar el tiempo de inicio del experimento
    inicio_experimento = time.time()
    
    # Crear un objeto de texto para mostrar el tiempo transcurrido
    texto_tiempo = visual.TextStim(win=win, text='', pos=(0, -0.25), height=0.1, color='white')
    
    import random
    
    # Generar una duración aleatoria entre 3 y 5 segundos
    duracion_cross = random.uniform(3, 5)
    
    # Guardar la duración en una variable que puedas utilizar en tu experimento
    thisExp.addData('duracion_cross', duracion_cross)
    # keep track of which components have finished
    ITIComponents = [cross]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            cross.setAutoDraw(True)
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + duracion_cross-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_iti
    win.color = original_color
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'bucle_estimuloexcitatorio_miedo_pds'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
