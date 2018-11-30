while not done:
    for event in pygame.event.get():
        # any other key event input
        if event.type == QUIT:
            done = True        
        elif event.type == KEYDOWN:
            if event.key == K_ESC:
                done = True

    vel_x = 0
    vel_y = 0
    speed = 1

    if pygame.key.get_mods() & KMOD_SHIFT
        speed = 2


    # get key current state
    keys = pygame.key.get_pressed()
    if keys[K_A]:
        vel_x = -1
    if keys[K_D]:
        vel_x = 1
    if keys[K_W]:
        vel_y = -1
    if keys[K_S]:
        vel_y = 1


    x_coord += vel_x * speed
    y_coord += vel_y * speed