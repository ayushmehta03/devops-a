
#############
#
#
#
#
#
# ##########

set -x #debug mode
set -e #exits script when there is an error
set -o pipefail



df -h

free -g


nproc

ps -ef | grep amazon | awk -F" " '{print $2}'