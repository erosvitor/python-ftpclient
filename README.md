## About
The project shows how to implement a FTP client using Python language.

## Starting the project

### Clonning the project
```
$ git clone https://github.com/erosvitor/python-ftpclient.git

$ cd python-ftpclient
```

### Testing the project
**Step 1:** Type the FTP data access in the file ftpclient.settings
```
{
  "dir_files" : "<folder-files>",
  "ftp_host" : "<ftpsever-host>",
  "ftp_port" : <ftpsever-port>,
  "ftp_user" : "<ftpsever-username>",
  "ftp_pass" : "<ftpsever-password>",
  "delay" : 1,
  "cyclic" : true
}
```

**Step 2:** Run the project with command below
```
$ python3 ftpclient.py
```

## License
This project is under license from MIT. For more details, see the LICENSE file.
