Option Explicit
Option Compare Text

Dim attempts As Integer

Private Sub UserForm_QueryClose(Cancel As Integer, CloseMode As Integer)
    If CloseMode = vbFormControlMenu Then Cancel = 1
End Sub

Private Sub CommandButton1_Click()
    Unload Me
    If Workbooks.Count > 0 Then
        ThisWorkbook.Close SaveChanges:=False
    Else
        Application.Quit
    End If
End Sub

Private Sub CommandButton2_Click()
    If TextBox1.Text = "" Or TextBox2.Text = "" Then
        MsgBox "Enter your Username/Password", vbInformation, "Login"
        Exit Sub
    End If
    
    If CheckCredentials(TextBox1.Text, TextBox2.Text) Then
        ActiveWorkbook.FollowHyperlink Address:="https://www.microsoft.com/ru-ru"
        Unload Me
    Else
        attempts = attempts + 1
        MsgBox "Incorrect password", vbExclamation, "Error"
        
        If attempts = 1 Then
            Label3.Caption = "You have 1 login attempt left"
        ElseIf attempts = 2 Then
            MsgBox "Your login attempts expired!", vbExclamation, "Error"
            Application.Quit
        End If
    End If
End Sub

Private Sub UserForm_Click()
End Sub

Private Function CheckCredentials(username As String, password As String) As Boolean
    CheckCredentials = (username = "admin" And password = "password")
End Function