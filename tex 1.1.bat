@if (@CodeSection == @Batch) @then


@echo off
set SendKeys=CScript //nologo //E:JScript "%~F0"
start "" /B cmd



set /p tex=ENTER TEXT:

:A

%SendKeys% "%tex%{ENTER}"


goto :A

@end 

// JScript section

var WshShell = WScript.CreateObject("WScript.Shell");
WshShell.SendKeys(WScript.Arguments(0));


