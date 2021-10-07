import sys
import subprocess
try:
    import requests
    import tkinter
    import json
    import tkinter.messagebox
    from bs4 import *
    import lxml
except:
    print("One or more required libraries is/are not installed, should I try to install them? (Type Y to install)")
    if input("Y/N--> ") == "y":
        subprocess.call([sys.executable, "-m" ,"pip", "install", "requests", "bs4", "lxml"])
        print("RUN ME AGAIN!")
        exit(0)

def loginfo(text : str):
    print("❔] " + text)

def logwarn(text : str):
    print("⚠️] " + text)

def logerror(text : str):
    print("❌] " + text)

def logsuccess(text : str):
    print("✔️] " + text)



class Command:
    def __init__(self, function, command : str, dependencies : list, helpmsg : str) -> None:
        self.function = function
        self.command = command
        self.deps = dependencies
        self.helpmsg = helpmsg

    def link(self):
        commandarray.append(self)

global running
running = Command(None, "None", [], "Not running anything")

try:
    window = tkinter.Tk()
    window.wm_withdraw()
    usetkinter = True
except:
    logwarn("No tkinter found/errored on launch! Falling back to logsystem.")
    usetkinter = False

#usetkinter = False

versioninfo = int(sys.version.split(" ")[0].split(".")[0] + sys.version.split(" ")[0].split(".")[1])
if not versioninfo > 3.7 and usetkinter: # gets 2nd digit from version string, i.e. from 3.8.10 it gets 8
    logwarn("Your tkinter doesn't support tkinter.messagebox! Falling back to logsystem.")
    usetkinter = False

def alertsuccess(msg:str):
    if usetkinter:
        tkinter.messagebox.showinfo(title="SkyPy running command " + running, message=msg)
    else:
        logsuccess(msg)


loginfo("ByzantineProcess's SkyPy Toolbox")


def loadbuiltindeps():
    loginfo("Getting data...")
    buypricesjson = requests.get(url="https://raw.githubusercontent.com/skyblockz/pricecheckbot/master/data.json").text
    bazaarjson = requests.get("https://api.hypixel.net/skyblock/bazaar").text
    loginfo("Loading and preparing data...")
    global buyprices
    global bazaar
    global sellprices
    buyprices = json.loads(buypricesjson)
    bazaar = json.loads(bazaarjson)
    sellpricespage = "<table style=\"width: 100%\"><tbody><tr><td>Products</td><td>NPC Sell</td></tr><tr><td>Wheat</td><td>1</td></tr><tr><td>Enchanted Bread</td><td>60</td></tr><tr><td>Hay Bale</td><td>9</td></tr><tr><td>Enchanted Hay Bale</td><td>1300</td></tr><tr><td>Carrot</td><td>1</td></tr><tr><td>Enchanted Carrot</td><td>160</td></tr><tr><td>Enchanted Carrot on a Stick</td><td>10240</td></tr><tr><td>Enchanted Golden Carrot</td><td>20608</td></tr><tr><td>Potato</td><td>1</td></tr><tr><td>Enchanted Potato</td><td>160</td></tr><tr><td>Enchanted Baked Potato</td><td>25600</td></tr><tr><td>Pumpkin</td><td>4</td></tr><tr><td>Enchanted Pumpkin</td><td>640</td></tr><tr><td>Melon</td><td>0.5</td></tr><tr><td>Enchanted Melon</td><td>160</td></tr><tr><td>Enchanted Glistering Melon</td><td>1000</td></tr><tr><td>Enchanted Melon Block</td><td>25600</td></tr><tr><td>Seeds</td><td>0.5</td></tr><tr><td>Enchanted Seeds</td><td>80</td></tr><tr><td>Red Mushroom</td><td>4</td></tr><tr><td>Enchanted Red Mushroom</td><td>640</td></tr><tr><td>Red Mushroom Block</td><td>4</td></tr><tr><td>Enchanted Red Mushroom Block</td><td>2300</td></tr><tr><td>Brown Mushroom</td><td>4</td></tr><tr><td>Enchanted Brown Mushroom</td><td>640</td></tr><tr><td>Brown Mushroom Block</td><td>4</td></tr><tr><td>Enchanted Brown Mushroom Block</td><td>2300</td></tr><tr><td>Cocoa Bean</td><td>3</td></tr><tr><td>Enchanted Cocoa Bean</td><td>480</td></tr><tr><td>Enchanted Cookie</td><td>61500</td></tr><tr><td>Cactus</td><td>1</td></tr><tr><td>Enchanted Cactus Green</td><td>160</td></tr><tr><td>Enchanted Cactus</td><td>25600</td></tr><tr><td>Sugar Cane</td><td>2</td></tr><tr><td>Enchanted Sugar</td><td>320</td></tr><tr><td>Enchanted Paper</td><td>384</td></tr><tr><td>Enchanted Sugar Cane</td><td>51200</td></tr><tr><td>Feather</td><td>3</td></tr><tr><td>Enchanted Feather</td><td>480</td></tr><tr><td>Leather</td><td>3</td></tr><tr><td>Enchanted Leather</td><td>1700</td></tr><tr><td>Raw Beef</td><td>4</td></tr><tr><td>Enchanted Raw Beef</td><td>640</td></tr><tr><td>Raw Porkchop</td><td>5</td></tr><tr><td>Enchanted Pork</td><td>800</td></tr><tr><td>Enchanted Grilled Pork</td><td>128000</td></tr><tr><td>Raw Chicken</td><td>4</td></tr><tr><td>Enchanted Raw Chicken</td><td>640</td></tr><tr><td>Enchanted Egg</td><td>432</td></tr><tr><td>Enchanted Cake</td><td>2700</td></tr><tr><td>Super Enchanted Egg</td><td>/</td></tr><tr><td>Mutton</td><td>5</td></tr><tr><td>Enchanted Mutton</td><td>800</td></tr><tr><td>Enchanted Cooked Mutton</td><td>128000</td></tr><tr><td>Raw Rabbit</td><td>4</td></tr><tr><td>Enchanted Raw Rabbit</td><td>640</td></tr><tr><td>Rabbit Foot</td><td>5</td></tr><tr><td>Rabbit Hide</td><td>5</td></tr><tr><td>Enchanted Rabbit Foot</td><td>800</td></tr><tr><td>Enchanted Rabbit Hide</td><td>2880</td></tr><tr><td>Nether Wart</td><td>3</td></tr><tr><td>Enchanted Nether Wart</td><td>480</td></tr><tr><td>Rotten Flesh</td><td>2</td></tr><tr><td>Enchanted Rotten Flesh</td><td>320</td></tr><tr><td>Bone</td><td>2</td></tr><tr><td>Enchanted Bone</td><td>320</td></tr><tr><td>Enchanted Bone Block</td><td>/</td></tr><tr><td>String</td><td>3</td></tr><tr><td>Enchanted String</td><td>576</td></tr><tr><td>Spider Eye</td><td>3</td></tr><tr><td>Enchanted Spider Eye</td><td>480</td></tr><tr><td>Enchanted Fermented Spider Eye</td><td>31000</td></tr><tr><td>Gunpowder</td><td>4</td></tr><tr><td>Enchanted Gunpowder</td><td>640</td></tr><tr><td>Enchanted Firework Rocket</td><td>41000</td></tr><tr><td>Ender Pearl</td><td>10</td></tr><tr><td>Enchanted Ender Pearl</td><td>200</td></tr><tr><td>Enchanted Eye of Ender</td><td>3520</td></tr><tr><td>Ghast Tear</td><td>16</td></tr><tr><td>Enchanted Ghast Tear</td><td>80</td></tr><tr><td>Slimeball</td><td>5</td></tr><tr><td>Enchanted Slimeball</td><td>800</td></tr><tr><td>Enchanted Slime Block</td><td>128000</td></tr><tr><td>Blaze Rod</td><td>9</td></tr><tr><td>Enchanted Blaze Powder</td><td>1440</td></tr><tr><td>Enchanted Blaze Rod</td><td>230400</td></tr><tr><td>Magam Cream</td><td>8</td></tr><tr><td>Enchanted Magam Cream</td><td>1280</td></tr><tr><td>Cobblestone</td><td>1</td></tr><tr><td>Enchanted Cobblestone</td><td>160</td></tr><tr><td>Coal</td><td>2</td></tr><tr><td>Enchanted Coal</td><td>320</td></tr><tr><td>Enchanted Charcoal</td><td>320</td></tr><tr><td>Enchanted Block of Coal</td><td>51000</td></tr><tr><td>Iron Ingot</td><td>3</td></tr><tr><td>Enchanted Iron</td><td>480</td></tr><tr><td>Enchanted Iron Block</td><td>76800</td></tr><tr><td>Gold Ingot</td><td>4</td></tr><tr><td>Enchanted Golden Carrot</td><td>640</td></tr><tr><td>Enchanted Gold Block</td><td>102000</td></tr><tr><td>Diamond</td><td>8</td></tr><tr><td>Enchanted Diamond</td><td>1280</td></tr><tr><td>Enchanted Diamond Block</td><td>204800</td></tr><tr><td>Lapis Lazuli</td><td>1</td></tr><tr><td>Enchanted Lapis Lazuli</td><td>160</td></tr><tr><td>Enchanted Lapis Block</td><td>25600</td></tr><tr><td>Emerald</td><td>6</td></tr><tr><td>Enchanted Emerald</td><td>960</td></tr><tr><td>Enchanted Emerald Block</td><td>153600</td></tr><tr><td>Redstone</td><td>1</td></tr><tr><td>Enchanted Redstone</td><td>160</td></tr><tr><td>Enchanted Redstone Block</td><td>25600</td></tr><tr><td>Nether Quartz</td><td>4</td></tr><tr><td>Enchanted Quartz</td><td>640</td></tr><tr><td>Enchanted Quartz Block</td><td>102400</td></tr><tr><td>Obsidian</td><td>12</td></tr><tr><td>Enchanted Obsidian</td><td>1920</td></tr><tr><td>Glowstone Dust</td><td>2</td></tr><tr><td>Enchanted Glowstone Dust</td><td>320</td></tr><tr><td>Enchanted Glowstone</td><td>61000</td></tr><tr><td>Gravel</td><td>3</td></tr><tr><td>Flint</td><td>4</td></tr><tr><td>Enchanted Flint</td><td>640</td></tr><tr><td>Ice</td><td>0.5</td></tr><tr><td>Packed Ice</td><td>4.5</td></tr><tr><td>Enchanted Ice</td><td>80</td></tr><tr><td>Enchanted Packed Ice</td><td>12800</td></tr><tr><td>Netherrack</td><td>1</td></tr><tr><td>Sand</td><td>2</td></tr><tr><td>Enchanted Sand</td><td>320</td></tr><tr><td>End Stone</td><td>2</td></tr><tr><td>Enchanted End Stone</td><td>320</td></tr><tr><td>Snowball</td><td>1</td></tr><tr><td>Snow Block</td><td>4</td></tr><tr><td>Enchanted Snow Block</td><td>600</td></tr><tr><td>Oak Wood</td><td>2</td></tr><tr><td>Enchanted Oak Wood</td><td>320</td></tr><tr><td>Spruce Wood</td><td>2</td></tr><tr><td>Enchanted Spruce Wood</td><td>320</td></tr><tr><td>Birch Wood</td><td>2</td></tr><tr><td>Enchanted Birch Wood</td><td>320</td></tr><tr><td>Dark Oak Wood</td><td>2</td></tr><tr><td>Enchanted Dark Oak Wood</td><td>320</td></tr><tr><td>Acacia Wood</td><td>2</td></tr><tr><td>Enchanted Acacia Wood</td><td>320</td></tr><tr><td>Jungle Wood</td><td>2</td></tr><tr><td>Enchanted Jungle Wood</td><td>320</td></tr><tr><td>Raw Fish</td><td>6</td></tr><tr><td>Enchanted Raw Fish</td><td>960</td></tr><tr><td>Enchanted Cooked Fish</td><td>150000</td></tr><tr><td>Salmon</td><td>10</td></tr><tr><td>Enchanted Raw Salmon</td><td>1600</td></tr><tr><td>Enchanted Cooked Salmon</td><td>256000</td></tr><tr><td>Clownfish</td><td>20</td></tr><tr><td>Enchanted Clownfish</td><td>3200</td></tr><tr><td>Pufferfish</td><td>15</td></tr><tr><td>Enchanted Pufferfish</td><td>2400</td></tr><tr><td>Prismarine Shard</td><td>5</td></tr><tr><td>Enchanted Prismarine Shard</td><td>400</td></tr><tr><td>Prismarine Crystals</td><td>5</td></tr><tr><td>Enchanted Prismarine Crystals</td><td>400</td></tr><tr><td>Clay</td><td>3</td></tr><tr><td>Enchanted Clay</td><td>480</td></tr><tr><td>Lily Pad</td><td>10</td></tr><tr><td>Enchanted Lily Pad</td><td>1600</td></tr><tr><td>Ink Sack</td><td>2</td></tr><tr><td>Enchanted Ink Sack</td><td>160</td></tr><tr><td>Sponge</td><td>50</td></tr><tr><td>Enchanted Sponge</td><td>2000</td></tr><tr><td>Enchanted Wet Sponge</td><td>80000</td></tr><tr><td>Carrot Bait</td><td>7</td></tr><tr><td>Minnow Bait</td><td>12</td></tr><tr><td>Fish Bait</td><td>20</td></tr><tr><td>Light Bait</td><td>16</td></tr><tr><td>Dark Bait</td><td>8</td></tr><tr><td>Spooky Bait</td><td>10</td></tr><tr><td>Spiked Bait</td><td>20</td></tr><tr><td>Blessed Bait</td><td>42</td></tr><tr><td>Ice Bait</td><td>3</td></tr><tr><td>Whale Bait</td><td>80</td></tr><tr><td>Revenant Flesh</td><td>/</td></tr><tr><td>Revenant Viscera</td><td>/</td></tr><tr><td>Tarantula Web</td><td>/</td></tr><tr><td>Tarantula Silk</td><td>/</td></tr><tr><td>Wolf Tooth</td><td>/</td></tr><tr><td>Golden Tooth</td><td>/</td></tr><tr><td>Hot Potato Book</td><td>13000</td></tr><tr><td>Compactor</td><td>640</td></tr><tr><td>Super Compactor 3000</td><td>50000</td></tr><tr><td>Summoning Eye</td><td>-</td></tr><tr><td>Protector Dragon Fragment</td><td>/</td></tr><tr><td>Old Dragon Fragment</td><td>/</td></tr><tr><td>Unstable Dragon Fragment</td><td>/</td></tr><tr><td>Strong Dragon Fragment</td><td>/</td></tr><tr><td>Young Dragon Fragment</td><td>/</td></tr><tr><td>Wise Dragon Fragment</td><td>/</td></tr><tr><td>Superior Dragon Fragment</td><td>/</td></tr><tr><td>Holy Dragon Fragment</td><td>/</td></tr><tr><td>Enchanted Redstone Lamp</td><td>30720</td></tr><tr><td>Enchanted Lava Bucket</td><td>50000</td></tr><tr><td>Hamster Wheel</td><td>20000</td></tr><tr><td>Foul Flesh</td><td>25000</td></tr><tr><td>Catalyst</td><td>500</td></tr><tr><td>Green Candy</td><td>/</td></tr><tr><td>Purple Candy</td><td>/</td></tr><tr><td>White Gift</td><td>/</td></tr><tr><td>Green Gift</td><td>/</td></tr><tr><td>Red Gift</td><td>/</td></tr><tr><td>Recombobulator 3000</td><td>-</td></tr><tr><td>Stock of Stonks</td><td>/</td></tr></tbody></table>"
    # hardcoded cause damn cloudflare doesnt let anything restricting cookies through, but its OK cuz these dont really change
    sellpricespage.replace(",", ".", -1)
    sellpricesoup = BeautifulSoup(sellpricespage, "lxml")
    sellprices = sellpricesoup.find_all("tr")
    sellprices.remove(sellprices[0])
    loginfo("Data loaded!")

commandarray = []

def loadbuiltincmd():
    loginfo("Loading builtin commands...")
    Command(help, "help", [], "Shows this message").link()
    Command(exit, "exit", [], "Exits SkyPy").link()
    Command(listdeps, "listdeps", [], "Shows lists of command dependencies").link()
    Command(revflip, "revflip", [], "Attemps to reverse-flip every item on the Bazaar").link()
    Command(revflipVerbose, "revflip -v", [], "revflip with extra logging").link()
    logsuccess("Builtin commands loaded. Ready for use!")


def help():
    loginfo("Help: ")
    for x in commandarray:
        loginfo(x.command + ": " + x.helpmsg)

def listdeps():
    loginfo("Dependencies: ")
    for x in commandarray:
        loginfo(x.command + ": " + str(x.deps))



def revflipVerbose():
    for x in list(sellprices):
        thename = x.find_all("td")[0]
        thename = str(thename.text).upper()
        thename = thename.replace(" ", "_")
        try:
            thesellprice = float(x.find_all("td")[1].text)
        except ValueError:
            logerror(thename + " isn't tradeable on the bazaar")
        try:
            thebuyprice = bazaar["products"][thename]["quick_status"]["buyPrice"]
            if thebuyprice < thesellprice:
                logsuccess("You can Bazaar-to-NPC Flip the " + thename)
                alertsuccess("You can Reverse Flip the " + thename.lower().replace("_", " "))
                loginfo(str("Pride diff: " + thesellprice - thebuyprice) + " - " + thename)
            if thebuyprice > thesellprice:
                logwarn("Can't revflip the " + thename)
        except KeyError:
            logerror(thename + " isn't tradeable on the bazaar")


def revflip():
    top_gap = 0.0
    tgname = ""
    for x in list(sellprices):
        thename = x.find_all("td")[0]
        thename = str(thename.text).upper()
        thename = thename.replace(" ", "_")
        try:
            thesellprice = float(x.find_all("td")[1].text)
        except ValueError:
            continue
        try:
            thebuyprice = bazaar["products"][thename]["quick_status"]["buyPrice"]
            if thebuyprice < thesellprice:
                logsuccess("You can Bazaar-to-NPC Flip the " + thename)
                alertsuccess("You can Reverse Flip the " + thename.lower().replace("_", " "))
                
                if thesellprice - thebuyprice > top_gap:
                    top_gap = thesellprice - thebuyprice
                    tgname = thename.lower().replace("_", " ")
            if thebuyprice > thesellprice:
                continue
        except KeyError:
            continue
    loginfo("The best item to revflip is " + tgname + " with a buy/sell difference of " + str(top_gap))


def runcmd(_input : str):
    for x in commandarray:
        if x.command == _input:
            global running
            running = _input
            getattr(x, "function")()


if __name__ == "__main__":
    loadbuiltindeps()
    loadbuiltincmd()
    while True:
        cmd = input("SkyShell--> ")
        runcmd(cmd)

        
