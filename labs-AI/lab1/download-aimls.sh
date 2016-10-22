#!/bin/bash

echo '\n AIML files download script ....'
URL="http://www.alicebot.org/aiml/aaa/"

if [ $# -eq 0 ]
	then
		echo "You haven't provided a file, so Bot.aiml will be downloaded"
		URL="${URL}/Bot.aiml"
		wget "${URL}" -P aiml/
	else
		echo "Downloading /$1"
		URL="${URL}/${1}.aiml"
		wget "${URL}" -P aiml/
fi


