if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/4kcinemas/Netflix-Bot /Coby
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Coby
fi
cd /Coby
pip3 install -U -r requirements.txt
echo "sᴛᴀʀᴛɪɴɢ 𝗗𝗞 𝗕𝗢𝗧𝘅........"
python3 bot.py
