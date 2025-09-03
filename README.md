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
Minimum Java Development Kit (JDK): Java 11

### Internet Access
OWASP dependency-check requires access to several externally hosted resources.
For more information see [Internet Access Required](https://dependency-check.github.io/DependencyCheck/data/index.html).

### Download the latest dependency-check CLI release:
The latest CLI can be downloaded from github in the [releases section](https://github.com/dependency-check/DependencyCheck/releases).

## Installation and Setup

### 1. Setting up the Graphical User Interface
  * Rename the downloaded DependencyCheckGUI release directory to `DependencyCheckGUI`.
  
  * Extract the downloaded Dependency-Check CLI release. Copy the `dependency-check` folder into the `DependencyCheckGUI` folder.
  
  * **(Important)** Place the `DependencyCheckGUI` folder on your Desktop. This is currently a requirement for the application to function correctly.
  
  * Navigate to the `dependency-check` folder and create a new text file named `NVD API Key.txt`.
  
  * Enter your NVD API Key into the `NVD API Key.txt` file. This will override the default (empty) key.
  
  * Ensure that both Python and the Java Development Kit are properly installed and configured on your system.
  
  * Open a command prompt or terminal and execute the following commands:
```
> cd .\Desktop\DependencyCheckGUI\Scripts\
> python "dependency-check GUI.py"
```


## Usage

### 1. Running Dependency-Check Scans (Default Mode)

  *  Fill in the required fields: `Project Name`, `Application Version`, and `Path` to the project you wish to scan.

  *  Optionally, enter a new NVD API key. Leave this field blank to use the key defined in the `NVD API Key.txt` file (recommended).

  *  Click the "Run Dependency-Check" button to start the scan.

  *  Access the generated reports by clicking the "Open Reports" button. The reports will be located in the reports folder.

  *  View the debugging logs by clicking the "View Logs" button.

### 2. Running Dependency-Check Scans (Update Only Mode)

  *  Optionally, enter a new NVD API key. Leave this field blank to use the key defined in the `NVD API Key.txt` file (recommended).

  *  Click the "Run Dependency-Check" button to initiate an update of the Dependency-Check CVE database using the latest NVD data.  The "Path", "Project Name" and "Application Version" fields are ignored in this mode.





   






