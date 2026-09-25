------------------------------------------------------------------------

    Appblocker - Created by Dylan Hawes - https://github.com/hawesd04

------------------------------------------------------------------------

Hello, welcome to AppBlocker, a Python tool that makes use of the system
hosts file to redirect the connection of certain applications and urls
to localhost, effectively blocking them from being accessed.

This is a productivity tool! It is meant to serve the purpose of entirely
restricting the access to distractions. You can either set it to work for
a predefined duration, or like an alarm for the blocking period to end at
a certain time.

------------------------------------------------------------------------

What you need to know:

* The Hosts File:
    - This is a system file that acts as a locally hosted DNS.
    - It essentially is the first place your computer looks for directions
      taking precedent over your DNS1, DNS2, or local connection.
    - In simple terms, it converts hostnames to IP addresses
    - To modify it, AppBlocker requires elevated permissions

* What specifically does this do?
    - This appends extra lines onto your hosts file setting the IP
      addresses for distracting sites/apps like twitter, discord, youtube,
      etc. to your localhost connection (127.0.0.1).
    - This makes any selected sites virtually inaccessible
    - Flushes the DNS between runs to ensure the change immediately applies
    
* Is this safe?
    - Yes, this is safe, this modifies your hosts file temporarily, and 
      immediately afterwards it deletes any lines it added, reverting your
      hosts file to its original state.
    - Nothing is done beyond that with the elevated permissions. In
      all actuality, this is a very simple piece of software.

* Why isn't it working?
    - This is likely a fault of your browser using something called "Secure DNS".
      if the program is failing to block addresses, ensure that in Privacy & Safety
      in whatever browser you are using, "Use secure DNS" is disabled as it will
      override any changes made to the hosts file.

------------------------------------------------------------------------

Installation instructions:

From the latest release on the AppBlocker GitHub repository, download the
provided AppBlocker.zip file. Extract it in an accessible directory.

From there you should see an _internal folder (containing assets relevant
to the GUI and program functionality), and an AppBlocker.exe

Launch AppBlocker.exe to run! By default, it determines whether you are 
using a Windows/Linux/MAC device, and assigns your default hosts file,
but in the case it fails to do so, you can navigate to your machine's
hosts file to select it. The program will NOT function unless the hosts
file is selected.

You can either select a duration or an end time. It will always take the
version most recently modified. From there, select which apps/sites you
wish to disable, and click the 

------------------------------------------------------------------------