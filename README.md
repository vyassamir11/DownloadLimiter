# DownloadLimiter
Shuts down the PC when a download limit is reached. Script written to limit my data usage while downloading
through my daily limited internet.


### It requires admin privileges to shutdown.
>On windows, you can invoke it from Admin Command Prompt or PowerShell. <br>
>On Linux and Mac, use sudo before the command.

### Usage
>First argument is data limit in MB and the second argument is time period of update in seconds.<br>
>The below will run the program with 1024 MB of limit and program will monitor usage after every 5 seconds.<br> 
```python download_limiter.py 1024 5```
