# Cron Job Tutorial

***Note:*** _This tutorial was generated with OpenAI Chat as an experiment. The prompt given was
"Please write a cronjob for ubuntu to log the date and time every 5 minutes. Explain the steps required to get it working"_

To create a cron job that logs the date and time every 5 minutes on an Ubuntu system, follow these steps:

Open a terminal window and type the following command to open the crontab file for editing:
```
sudo crontab -e
```
This will open the crontab file in the default text editor for your system.

Add the following line to the end of the file, replacing /path/to/log/file.log with the desired path and file name for the log file:
```
*/5 * * * * date >> /path/to/log/file.log
```
This line tells cron to execute the date command every 5 minutes (*/5), and append the output to the specified log file.

Save the file and exit the text editor. The cron job will now run every 5 minutes.
Note: If you want to use a different command instead of date, you can simply replace date with the desired command.

You can also use the crontab command to view and manage your cron jobs. For example, to view your current cron jobs, you can use the following command:

```
crontab -l
```
To remove all of your cron jobs, you can use the following command:

```
crontab -r
```
For more information about cron and crontab, you can refer to the crontab man page by running man crontab in a terminal window.


Based on another answer given by OpenAI Chat, the cronjob has been modified to:

```
*/5 * * * * i=0; do i=$((i+1));done; date $i >> /remotelabs/SBC_TESTLOG.log
```
With the aim of adding an incrementing number to the start of each line in the log file.
