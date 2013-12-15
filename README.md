# automator-workflows

Yet another repo of Automator actions/workflows for Mac OS X.

## Show Time in Local Time Zone

Mac OS X text service to show time in selected text in local time
zone. Result is shown as a Notification Center notification.

### Installation

```
$ mkdir -p ~/Library/Services
$ cp -r services/Show\ Time\ in\ Local\ Time\ Zone/Show\ Time\ in\ Local\ Time\ Zone.workflow ~/Library/Services/
```

### Example


1. Select the text below and right-click to bring up the context menu.

```
13:00 UTC
3pm PST
10am JST
```

2. Choose "Show Time in Local Time Zone"
