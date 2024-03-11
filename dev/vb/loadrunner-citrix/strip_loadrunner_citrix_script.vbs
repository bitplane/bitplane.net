'
' Removes unused png, xml and inf files from the data/snapshots dir
' of a LoadRunner Citrix script.
'
' Make a backup before running it.
'

answer = msgbox("This will permanently delete files from all scripts in this directory!" & vbcrlf & "Are you sure?!", vbYesNo or vbDefaultButton2 or vbExclamation, "WAIT A MINUTE!")

if answer = vbNo then
  wscript.quit -1
end if

set fso = createobject("scripting.filesystemobject")
set cd = fso.getFolder(".")

delcount = 0
keepcount = 0

' loop through each LoadRunner script
for each d in cd.subfolders

  ' store the names we want to keep in a dict
  set dict = createobject("scripting.dictionary")

  ' find c files
  for each f in d.files

    if len(f.name) > 2 and right(f.name, 2) = ".c" then

      ' open the file...
      set fin = f.openAsTextStream()

      ' read the file
      while fin.atEndOfStream = False

        ' read each line
        s = fin.readLine()

        ' look for the word "snapshot"
        ' case insensitive because we want to match "regionSnapshot" too
        ' apologies for not using regex here, but it's quicker for me to do it this way
        p = instr(ucase(s), "SNAPSHOT")

        ' if we found it
        if (p > 0) then

          ' get the start of the number
          p = p + 8

          num = Empty

          ' copy it
          while isNumeric(mid(s,p,1))
            num = num & mid(s,p,1)
            p = p + 1
          wend

          ' add the number to the dictionary 
          if dict.exists(num) = false then
            dict.add num, true
          end if

        end if ' line contains a snapshot

      wend ' reading c file

    end if ' is a c file

  next ' each file in script dir


  ' now open the data/snapshots directory
  if fso.folderexists(".\" & d.name & "\data\snapshots") then

    set snapdir = fso.getFolder(".\" & d.name & "\data\snapshots")

    ' and loop through each file  
    for each f in snapdir.files

      p = instr(ucase(f.name), "SNAPSHOT")

      ' if we found it
      if (p > 0) then

        ' get the start of the number
        p = p + 8

        num = Empty

        ' copy it
        while isNumeric(mid(f.name,p,1))
          num = num & mid(f.name,p,1)
          p = p + 1
        wend

        ' we can delete the file
        if dict.exists(num) = false then
          f.delete
          delcount = delcount + 1
        else
          keepcount = keepcount + 1
        end if

      else
        keepcount = keepcount + 1
      end if

    next ' snapshot file

  end if ' folder exists

next ' script in current directory


msgbox "Deleted " & delcount & " and kept " & keepcount & " files."