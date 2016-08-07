
echo on

start cmd /c "cd /d "%ProgramFiles%\Docker Toolbox" & start sh.exe --login -i "%ProgramFiles%\Docker Toolbox\start.sh""

:: access with relative path (Win vs Linux format ...)
	::start cmd /c "(type "%ProgramFiles%\Docker Toolbox\start.sh" && echo cd ../../../%cd%) > file.sh & start sh.exe --login -i "file.sh""
:: access with cygpath ?
	:: -c 'cd "$(cygpath "%cd%")"; exec bash'
:: edit .bashrc ?
	:: echo %cd% >> ~/.bashrc
:: bypass trap ? - in start.sh - reference: https://www.gnu.org/software/bash/manual/html_node/Special-Parameters.html
	::start cmd /k "(echo true && type "%ProgramFiles%\Docker Toolbox\start.sh") > file.sh & start sh.exe --login -i "file.sh""
