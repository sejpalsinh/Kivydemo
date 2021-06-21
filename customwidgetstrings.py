def getUserInputStr(placeHolder,helperText,xPosition,yPosition,widthSize):
    posStr ="""'center_x':{xPos},'center_y':{yPos}""".format(xPos=xPosition,yPos=yPosition)
    posStr = "{"+posStr+"}"
    getUserInputString = """MDTextField:
            hint_text : "{placeHolderTxt}"
            helper_text : "{helperTxt}"
            helper_text_mode: 'on_focus'
            pos_hint:{posStr}
            size_hint_x:None
            width:{widthSize}
    """
    getUserInputString = getUserInputString.format(placeHolderTxt =placeHolder,helperTxt=helperText,widthSize=widthSize,posStr=posStr)
    return  getUserInputString
