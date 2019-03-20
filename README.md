# llsdn

An lldb plugin for ShadowNode and JerryScript, which enables inspection of JavaScript states for insights into ShadowNode processes and their core dumps.

### Install Instructions

#### Prerequisites: Install LLDB and its Library

To use llsdn you need to have the LLDB debugger installed. The recommended version is LLDB 3.9 and above.

- OS X/macOS

  - You can install Xcode and use the LLDB that comes with it.

- Linux

  - You can install the lldb package using the package manager of your distribution. You may need to install additional packages for liblldb as well.

  - For example, on Ubuntu 16.04 you can install the prerequisites with

    `apt-get install lldb-4.0 liblldb-4.0-dev`

#### Install the Plugin

###### Install llnode globally via npm

If you have `lldb` available on your `PATH`, simply run:

```
npm install -g llsdn
```

After installing with npm, append following line in your `~/.lldbinit`:

```
command script import <replace with 'npx llsdn' output>
```
