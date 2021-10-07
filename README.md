## About
The project shows how to implement a FTP client using Python language.

## Technologies
The following tools were used in this project:

* [Python](https://www.python.org/)

## Requirements
Before starting this project you need to have Git and Python 3 installed.

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

## Release History

* 1.0.0 (2021-05-04)
    * First version
