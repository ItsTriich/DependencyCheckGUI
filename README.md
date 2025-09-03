# Dependency-Check Graphical User Interface (Windows)
Dependency-Check GUI is a user friendly interface for the OWASP Dependency-Check CLI tool. Developed with Python’s standard modules. This GUI allows developers and security analysts to run vulnerability scans on project dependencies with ease, no command-line gymnastics or third-party libraries.

Dependency-Check is a Software Composition Analysis (SCA) tool that attempts to detect publicly disclosed vulnerabilities contained within a project's dependencies. It does this by determining if there is a Common Platform Enumeration (CPE) identifier for a given dependency. If found, it will generate a report linking to the associated CVE entries.

## Notice
This product uses the NVD API but is not endorsed or certified by the NVD.

### NVD API Key Highly Recommended

Dependency-check has moved from using the NVD data-feed to the NVD API.
Users of dependency-check are **highly** encouraged to obtain an NVD API Key; see https://nvd.nist.gov/developers/request-an-api-key
Without an NVD API Key dependency-check's updates will be **extremely slow**.
Please see the documentation for the cli integrations on
how to set the NVD API key.

## Requirements

### Python Verison
Python 3.13.x

### Java Verison
Minimum Java Development Kit: Java 11

### Internet Access
OWASP dependency-check requires access to several externally hosted resources.
For more information see [Internet Access Required](https://dependency-check.github.io/DependencyCheck/data/index.html).

### Download the latest dependency-check CLI release:
The latest CLI can be downloaded from github in the [releases section](https://github.com/dependency-check/DependencyCheck/releases).

## Instructions

### 1. Setting up the Graphical User Interface
  * Rename the DependencyCheckGUI release -> DependencyCheckGUI
  * Unzip and open the recently downloaded Dependency-Check CLI release. Copy the "dependency-check" folder into the DependencyCheckGUI folder.
  * (REQUIRED) The DependencyCheckGUI folder must be located on the desktop.
  * Navigate into "dependency-check" and create a file named "NVD API Key.txt"
  * Input your API Key into this text document.
  * Verify that Python and the Java Development Kit are installed.
  * Run these commands:
```
Powershell
> cd .\Desktop\DependencyCheckGUI\Scripts\
> python "dependency-check GUI.py"
```

> .\bin\dependency-check.bat -h




