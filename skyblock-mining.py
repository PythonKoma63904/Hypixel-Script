import minescript
import keyboard
import mouse
import time

def count_enchanted_cobble():
    inventory = minescript.player_inventory()
    enchanted_cobble_count = 0
    for item in inventory:
        if item is not None and (getattr(item, "name", None) == "minecraft:cobblestone" or getattr(item, "item", None) == "minecraft:cobblestone"):
            if hasattr(item, "custom_name") and "Enchanted Cobblestone" in str(item.custom_name):
                enchanted_cobble_count += item.count
            elif hasattr(item, "nbt") and "Enchanted Cobblestone" in str(item.nbt):
                enchanted_cobble_count += item.count
    return enchanted_cobble_count

def mine_cobblestone_until_enchanted(target_count=1664):
    minescript.echo(f"Mining until you have {target_count} Enchanted Cobblestone...")
    while True:
        if keyboard.is_pressed("F7"):
            minescript.echo("Script exited.")
            release_all_keys()
            exit()
        if keyboard.is_pressed("F6"):
            minescript.echo("Mining paused. Press F6 to resume.")
            release_all_keys()
            while keyboard.is_pressed("F6"):
                time.sleep(0.05)
            return  # Return to main loop to wait for resume
        minescript.player_press_sneak(True)
        minescript.player_press_attack(True)
        minescript.player_press_forward(True)
        minescript.player_set_orientation(270, -90)
        time.sleep(0.05)
        if count_enchanted_cobble() >= target_count:
            release_all_keys()
            break

def sell():
    minescript.execute(command="/warp hub")
    time.sleep(3)
    minescript.player_press_forward(True)
    time.sleep(1.35)
    minescript.player_press_forward(False)
    time.sleep(0.5)
    minescript.player_set_orientation(90, 1)
    time.sleep(0.5)
    minescript.player_press_forward(True)
    time.sleep(5.5)
    minescript.player_press_forward(False)
    minescript.player_press_forward(True)
    minescript.player_press_jump(True)
    time.sleep(0.3)
    minescript.player_press_jump(False)
    minescript.player_press_forward(False)
    time.sleep(0.25)
    minescript.player_press_use(True)
    minescript.player_press_use(False)
    time.sleep(1)
    mouse.move(888, 533)
    mouse.click("left")
    time.sleep(0.5)
    mouse.move(889, 445)
    time.sleep(0.2)
    mouse.click("left")
    time.sleep(0.5)
    keyboard.press_and_release("esc")
    time.sleep(0.5)
    minescript.execute(command="/warp home")
    time.sleep(3)
    minescript.player_press_jump(True)
    time.sleep(0.1)
    minescript.player_press_jump(False)
    time.sleep(0.1)
    minescript.player_press_jump(True)
    time.sleep(0.1)
    minescript.player_press_jump(False)

def release_all_keys():
    minescript.player_press_sneak(False)
    minescript.player_press_attack(False)
    minescript.player_press_forward(False)

minescript.echo("Press F6 to start/pause. Press F7 to exit.")

running = False
while True:
    if keyboard.is_pressed("F7"):
        minescript.echo("Script exited.")
        release_all_keys()
        break
    if keyboard.is_pressed("F6"):
        running = not running
        if running:
            minescript.echo("Script started.")
            minescript.execute(command="/warp home")
            time.sleep(1)
            minescript.player_press_jump(True)
            time.sleep(0.1)
            minescript.player_press_jump(False)
            time.sleep(0.1)
            minescript.player_press_jump(True)
            time.sleep(0.1)
            minescript.player_press_jump(False)
            time.sleep(0.1)
        else:
            minescript.echo("Script paused. Press F6 to resume or F7 to exit.")
            release_all_keys()
        while keyboard.is_pressed("F6"):
            time.sleep(0.05)
    while running:
        mine_cobblestone_until_enchanted(1664)
        sell()
        if keyboard.is_pressed("F6"):
            running = False
            minescript.echo("Script paused. Press F6 to resume or F7 to exit.")
            release_all_keys()
            while keyboard.is_pressed("F6"):
                time.sleep(0.05)
            break
        if keyboard.is_pressed("F7"):
            minescript.echo("Script exited.")
            release_all_keys()
            exit()