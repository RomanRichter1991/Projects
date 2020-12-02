extends KinematicBody2D

# Declare basic physics:
const GRAVITY = 50
const WALKSPEED = 200
const JUMPHEIGHT = -800
var motion = Vector2()


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _physics_process(delta):
	move_and_slide(motion,Vector2(0,-1))
	
	#basic movement
	#if Input.is_key_pressed():
	#	pass
	if Input.is_action_pressed("ui_left"):
		motion.x = -WALKSPEED
	elif Input.is_action_pressed("ui_right"):
		motion.x = +WALKSPEED
	else:
		motion.x = 0
	
	#floor check and gravity
	if self.is_on_floor():
		print ("on floor")
		motion.y = 0
		if Input.is_action_pressed("ui_up"):
			motion.y = JUMPHEIGHT
			pass
	else:
		print ("not on floor")
		motion.y += GRAVITY
	
	
	print (motion.y)
	
	pass
