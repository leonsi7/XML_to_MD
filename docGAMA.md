## Abstract Unity Player

### player_perception_cone


**Result**: Wait for the connection of a unity client and send the paramters to the client

**Returns**: None

---
## Abstract Unity Linker

### init_species_to_send

- *species_list* (list)

**Result**: Initialize the species to send to unity

**Returns**: None

---
### send_message

- *players* (list)
- *mes* (map)

**Result**: send a message to the Unity Client

**Returns**: None

---
### send_world


**Result**: send the current state of the world to the Unity Client

**Returns**: None

---
### send_geometries

- *geoms* (list)
- *heights* (list)
- *players* (list)
- *geometry_colliders* (list)
- *is_3D* (list)
- *is_interactables* (list)
- *names* (list)
- *colors* (list)
- *tags* (list)

**Result**: send the background geometries to the Unity client

**Returns**: None

---
### send_init_data

- *id* (string)

**Result**: Wait for the connection of a unity client and send the paramters to the client

**Returns**: None

---
### after_sending_world

- *map_to_send* (map)

**Result**: Action trigger just after sending the world to Unity 

**Returns**: None

---
### after_sending_geometries


**Result**: Action trigger just after sending the background geometries to Unity 

**Returns**: None

---
### create_init_player

- *id* (string)

**Result**: Create and init a new unity player agent

**Returns**: None

---
### create_player

- *id* (string)

**Result**: Create a new unity player agent

**Returns**: None

---
### filter_distance

- *ags* (list)
- *player* (agent)

**Result**: Action called by the send_world action that returns the sub-list of agents to send to Unity from a given list of agents according to a max distance to the player

**Returns**: None

---
### message_agents

- *ags* (list)

**Result**: Action called by the send_world action that returns the message to send to Unity (as a list of map)

**Returns**: None

---
### filter_overlapping

- *ags* (list)
- *player* (agent)

**Result**: Action called by the send_world action that returns the sub-list of agents to send to Unity from a given list of agents according to a min proximity to the other agents to send

**Returns**: None

---
### new_player_location

- *loc* (point)
- *player* (agent)

**Result**: Action called by the move_player action that returns the location to send to Unity from a given player location

**Returns**: None

---
### move_player

- *player* (agent)
- *loc* (point)

**Result**: move the player agent

**Returns**: None

---
### move_player_external

- *id* (string)
- *x* (int)
- *y* (int)
- *angle* (int)

**Result**: move the player agent 

**Returns**: None

---
### send_player_position

- *player* (agent)

**Result**: send the new position of the player to Unity (used to teleport the player from GAMA) 

**Returns**: None

---
### add_to_send_parameter

- *map_to_send* (map)

**Result**: add values to the parameters sent to the Unity Client

**Returns**: None

---
### send_parameters

- *player* (agent)

**Result**: Send the parameter to Unity to intialized the connection

**Returns**: None

---
### add_background_data

- *geoms* (list)
- *names* (list)
- *tag* (string)
- *is_3D* (boolean)
- *is_interactable* (boolean)
- *height* (float)
- *color* (rgb)
- *collider* (boolean)

**Result**: Add background geometries from a list of geometries,a optional list of name (one per geometry), their heights, their collider usage, and an optional tag

**Returns**: None

---
### loc_to_send


**Result**: None

**Returns**: the location to send to Unity

---
### add_to_map

- *map* (map)
- *ag* (agent)

**Result**: None

**Returns**: other elements than the location to add to the data sent to Unity

---
### to_map

- *precision* (int)
- *ag* (agent)

**Result**: None

**Returns**: a map containing all the information to sent to unity concerning an agent

---
