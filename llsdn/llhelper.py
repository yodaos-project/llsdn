def get_selected_frame(debugger):
    target = debugger.GetTargetAtIndex(0)
    process = target.GetProcess()
    thread = process.GetSelectedThread()
    frame = thread.GetSelectedFrame()
    return frame
