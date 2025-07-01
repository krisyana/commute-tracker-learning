# 🎯 Terminal Aliases Quick Reference

A quick reference guide for all the useful aliases in your terminal setup.

## 📁 Navigation
```bash
..          # cd ..
...         # cd ../..
....        # cd ../../..
~           # cd ~
-           # cd - (previous directory)
dev         # cd ~/projects
home        # cd ~
```

## 📋 File Operations
```bash
ll          # ls -la (detailed listing)
la          # ls -A (show hidden files)
l           # ls -CF (compact listing)
lsd         # ls -la | grep '^d' (directories only)
lsf         # ls -la | grep '^-' (files only)
cp          # cp -i (interactive)
mv          # mv -i (interactive)
rm          # rm -i (interactive)
mkdir       # mkdir -p (recursive)
```

## 🐍 Python
```bash
python      # python3
pip         # pip3
py          # python3
py3         # python3
venv        # python3 -m venv
activate    # source venv/bin/activate
```

## 🔧 Git
```bash
g           # git
ga          # git add
gc          # git commit
gp          # git push
gl          # git pull
gs          # git status
gd          # git diff
gco         # git checkout
gcb         # git checkout -b
gb          # git branch
glog        # git log --oneline --graph --decorate
gst         # git stash
gstp        # git stash pop
gac         # git add . && git commit -m
gacp        # git add . && git commit -m && git push
gundo       # git reset --soft HEAD~1
gclean      # git clean -fd
```

## 🐳 Docker
```bash
d           # docker
dc          # docker-compose
dps         # docker ps
dpsa        # docker ps -a
di          # docker images
dex         # docker exec -it
dlog        # docker logs
dcup        # docker-compose up
dcdown      # docker-compose down
dcbuild     # docker-compose build
dcrestart   # docker-compose restart
dclogs      # docker-compose logs -f
```

## ⚡ Quick Commands
```bash
c           # clear
h           # history
j           # jobs -l
k           # kill -9
q           # exit
reload      # source ~/.zshrc
refresh     # source ~/.zshrc
```

## 🌐 System
```bash
myip        # curl -s https://ipinfo.io/ip
weather     # curl -s wttr.in
speedtest   # speed test
update      # sudo apt update && sudo apt upgrade -y
cleanup     # sudo apt autoremove && sudo apt autoclean
ports       # netstat -tulanp
ping        # ping -c 5
pingg       # ping google.com
```

## 📊 Monitoring
```bash
top         # htop
mem         # free -h
disk        # df -h
cpu         # lscpu | grep 'Model name'
psg         # ps aux | grep
meminfo     # free -h
cpuinfo     # lscpu
diskusage   # df -h
```

## 🌐 Development Servers
```bash
serve       # python3 -m http.server 8000
serve-3000  # python3 -m http.server 3000
serve-8080  # python3 -m http.server 8080
serve-9000  # python3 -m http.server 9000
serve-php   # php -S localhost:8000
serve-node  # npx serve .
serve-python # python3 -m http.server
serve-ruby  # ruby -run -e httpd . -p 8000
```

## 📦 Package Management
```bash
install     # sudo apt install
remove      # sudo apt remove
search      # apt search
show        # apt show
```

## 🔧 Config Files
```bash
zshconfig   # code ~/.zshrc
ohmyzsh     # code ~/.oh-my-zsh
bashconfig  # code ~/.bashrc
vimconfig   # code ~/.vimrc
gitconfig   # code ~/.gitconfig
```

## 📅 Utilities
```bash
now         # date +'%Y-%m-%d %H:%M:%S'
today       # date +'%Y-%m-%d'
week        # date +%V
month       # date +%B
path        # echo $PATH | tr ':' '\n'
```

## 🛡️ Safety
```bash
rm          # rm -i (interactive)
cp          # cp -i (interactive)
mv          # mv -i (interactive)
ln          # ln -i (interactive)
```

## 🎨 Colors
```bash
grep        # grep --color=auto
egrep       # egrep --color=auto
fgrep       # fgrep --color=auto
```

## 📝 Node.js (if using)
```bash
n           # npm
ni          # npm install
nid         # npm install --save-dev
nr          # npm run
nrb         # npm run build
nrs         # npm run start
nrt         # npm run test
```

## 🧶 Yarn (if using)
```bash
y           # yarn
ya          # yarn add
yad         # yarn add --dev
yr          # yarn run
yrb         # yarn run build
yrs         # yarn run start
yrt         # yarn run test
```

---

## 🚀 Most Used Workflows

### Daily Development
```bash
# Start work
dev
ll
gs

# Make changes
ga .
gc -m "Update feature"
gp

# Start server
serve
```

### Python Project Setup
```bash
mkdir myproject
cd myproject
venv venv
activate
pip install package_name
```

### Docker Workflow
```bash
dps
dcup
dclogs
dcdown
```

### System Maintenance
```bash
update
cleanup
mem
disk
```

---

**💡 Tip**: Use `alias` to see all available aliases in your terminal! 