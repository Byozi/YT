
# ⚡️ Getting Started [[Documentation](https://notreallyshikhar.gitbook.io/yukkimusicbot/)]
Checkout [Docs](https://notreallyshikhar.gitbook.io/yukkimusicbot/deployment/local-hosting-or-vps) for Detailed Explanation on VPS Deploy

Local Hosting or VPS
Supports Debian Based Only!
🚀 Deploying with Legacy Method:
Get ready with atleast  in a .env  file.
Not Getting? ​
1.  Upgrade and Update:
sudo apt-get update && sudo apt-get upgrade -y
2. Installing Required Packages:
sudo apt-get install python3-pip ffmpeg -y
3. Setting up PIP
sudo pip3 install -U pip
4. Installing Node
curl -fssL https://deb.nodesource.com/setup_17.x | sudo -E bash - && sudo apt-get install nodejs -y && npm i -g npm
5. Clone the Repository
git clone https://github.com/notreallyshikhar/YukkiMusicBot &&  cd YukkiMusicBot
6. Install Requirements
pip3 install -U -r requirements.txt
7. Create .env  with sample.env
cp sample.env .env
Edit .env with your vars 
8. Editing Vars:
vi .env
Edit .env with your values or you can simple copy a and paste it to your notepad, then edit and paste there.
Press I button on keyboard to start editing.
Press Ctrl + C  once you are done with editing vars and type :wq to save .env or :qa to exit editing.
9. Finally Run Yukki Music Bot
bash start
