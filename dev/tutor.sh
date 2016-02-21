#!/usr/bin/env bash

function ccat(){
    /usr/local/bin/ccat --bg=dark --color=always $* | less -NR
}


MAGENTA=$"\033[1;36m"
GREEN=$"\033[1;32m"
RED=$"\033[1;31m"
LF="`echo $'\n '`"
PREPROMPT=$'\e[31m>>>\e[0m'
RESET=$"\033[0m"
HR='----------------------------------------------'
echo -e "${MAGENTA}"
echo -e "Hi this is a simple tutorial for pjq..."
echo -e "When you see ${PREPROMPT} ${MAGENTA} hit ENTER to continue."
read -p "`echo $''`${PREPROMPT}"
clear

echo -e "${GREEN} --- WE WILL START WITH JSON ARRAYS --- ${RESET}"
clear

echo -e "Lets see the example Users.json"
read -p "`echo $''`${PREPROMPT}"
ccat tests/examples/users.json | less -N -R
clear


echo -e This command will dump the ${RED}first${RESET} user
echo -e "${GREEN} $ ./pjq tests/examples/users.json [0] ${RESET}"
read -p "`echo $''`${PREPROMPT}"
./pjq  tests/examples/users.json [0] | ccat
echo
clear

echo -e You can also use unix pipes.
echo -e "${GREEN} $ cat tests/examples/users.json  | ./pjq  [0] ${RESET}"
read -p "`echo $''`${PREPROMPT}"
cat tests/examples/users.json  | ./pjq  [0] | ccat
echo
clear


echo -e This command will dump the first ${RED}two${RESET} users
echo -e "${GREEN} $ cat tests/examples/users.json  | ./pjq  [0:2] ${RESET}"
read -p "`echo $''`${PREPROMPT}"
cat tests/examples/users.json  | ./pjq  [0:2] | ccat
echo
clear


echo -e This command will dump the first ${RED}3rd${RESET} and ${RED}5th${RESET} users
echo -e "${GREEN} $ cat tests/examples/users.json  | ./pjq  [3,5] ${RESET}"
read -p "`echo $''`${PREPROMPT}"
cat tests/examples/users.json  | ./pjq  [3,5] | ccat
echo
clear





echo
echo -e "${GREEN} --- NOW GO ON WITH JSON OBJECTS --- ${RESET}"
read -p "`echo $''`${PREPROMPT}"
echo
clear


echo -e "Lets see the example dummy.json"
read -p "`echo $''`${PREPROMPT}"
ccat tests/examples/dummy.json
clear


echo -e This command will dump the ${RED}reason${RESET} property
echo -e "${GREEN} $ ./pjq tests/examples/dummy.json reason ${RESET}"
read -p "`echo $''`${PREPROMPT}"
./pjq tests/examples/dummy.json reason | ccat
echo
clear


echo -e This command will dump the ${RED}response${RESET} property
echo -e "${GREEN} $ ./pjq tests/examples/dummy.json response ${RESET}"
read -p "`echo $''`${PREPROMPT}"
./pjq tests/examples/dummy.json response | ccat
echo
clear
