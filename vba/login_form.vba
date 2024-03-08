Dim Err As Integer

Private Sub UserForm1_QueryClose(Cancel As Integer, CloseMode As Integer)
  If CloseMode = 0 Then Cancel = 1
End Sub

Private Sub CommandButton1_Click()
  Unload UserForm1
  If Workbooks.Count > 1 Then
    ThisWorkbook.Close (0)
  Else
    Application. Quit
  End If
End Sub

Private Sub CommandButton2_Click()
  Dim i As Byte
  If Textbox1.Text = "" And TextBox2.Text = "" Then Exit Sub
  If Textbox1.Text = "" Or TextBox2.Text = "" Then
    MsgBox "Enter your Username/Password", vbInformation, "Login"
    Exit Sub
  End If
  With Лист3
    If Textbox1.Text = .Cells(1, 1) And TextBox2.Text = .Cells(1, 2) Then
      ActiveWorkbook.FollowHyperlink _
      Address:="https://www.microsoft.com/ru-ru"
      Unload UserForm1
    Else
      Err = Err + 1
      MsgBox "Incorrect password", vbExclamation, "Error"
    End If
    If Err = 1 Then
      Label3 = "You have 1 login attempts left"
    ElseIf Err = 2 Then
      MsgBox "Your login attempts expired!", vbExclamation, "Error"
      Application.Quit
    End If
  End With
End Sub

Private Sub UserForm Click()