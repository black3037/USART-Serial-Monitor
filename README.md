<p align="center">
  <img src="https://raw.githubusercontent.com/black3037/USART-Serial-Monitor/master/Images/monitor_window.PNG" alt="serialmonitor"/>
</p>

A multi-platform (OSX,LINUX coming soon) graphical interface debugging USART serial connections.
The UI can send and recieve messages from USART serial (possibly others protocalls as well, has not been tested yet).
This UI assumes strings sent from the command line are new line \n deliminted. This can easily be changed in the code.

Thie UI was tested with a ST32F4 Discovery board using USART. The Discovery board listens for messages termined by the new line character '\n' and echos them back over serial.



