# Munki Promote

This Python script will allow the user to set it up to automatically (with Jenkins) check their Munki Repository and change the catalog based off the last modified time. As of the latest update, multiple catalogs can be defined. Each section is treated as a catalog and you define what you want to promote and from what catalog. Currently the Munki team is discussing a way to incorporate this into the pkginfo files via an `autopromote` argument to the `makecatalogs` function. You can join in the conversation [here](https://groups.google.com/forum/#!topic/munki-dev/FKWmj4i-VEU/discussion)

## Requirements

- munki
- python
- access to your repo

## Setup

Adjust the variables in the config.py settings file.

## Jenkins Config

What I like to do is configure this to automatically work with Jenkins. This file is now an executable so you can actually just export the path of where you synced the repository (ex. /Users/macadmin/Documents/munki-promote) by using this command:

```
export PATH=$PATH:/Users/macadmin/Documents/munki-promote
```

Put this at the beginning of your job script and you won't have to worry about adding it permanently.
