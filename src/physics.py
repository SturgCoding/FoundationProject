
#-----------------------------------------------------------------
# ==========================================
# Code Base - Set response when this file is run
# ==========================================
PIXELS_PER_METER = 100  # 100 pixels = 1 meter

GRAVITY = 9.81

class PhysicsBody:
    def __init__(self, x, y, mass = 1.0):
        self.x = float(x)
        self.y = float(y)
        self.mass = mass

        self.ax = 0.0 #horizontal acceleration
        self.ay = GRAVITY #vertical acceleration (gravity)
        
        self.vx = 0.0 #horizontal velocity
        self.vy = 0.0 #vertical velocity

        self.ux = 0.0 #horizontal velocity before update
        self.uy = 0.0 #vertical velocity before update

        self.sx = 0.0 #horizontal displacement (from launch point)
        self.sy = 0.0 #vertical displacement (from launch point) 

        self.t = 0.0 #time since launch

        self._launch_x = float(x) #initial x position (launch point)
        self._launch_y = float(y) #initial y position (launch point)

        self.in_flight = False # is it in the air or not
        self.grounded = False # is it on the ground or not

        #call this when you drop or throw the can, vxms and vyms are the velocities in m/s
    def release(self, vx_ms = 0.0, vy_ms = 0.0):
        self.ux = vx_ms#launch velocisy, the "u" in suvat, it never changes 
        self.uy = vy_ms
        self.vx = vx_ms
        self.vy = vy_ms

        self.t = 0.0
        self.sx = 0.0
        self.sy = 0.0

        self._launch_x = self.x #remember the launch point(in px)
        self._launch_y = self.y

        self.in_flight = True #physics are now active(when u call release)
        self.grounded = False

        #this runs every frame(60fps)
    def update(self, dt):
        #dt is delta time, how many seconds have passed since the last frame, around 0.016s for us
        if not self.in_flight:
            return #if it's not in the air, don't update physics
        self.t += dt #add the time

            #v = u + at (live)
        self.vx = self.ux + self.ax * self.t
        self.vy = self.uy + self.ay * self.t

        #s = ut + 0.5at^2 (displacement from launch point)
        self.sx = self.ux * self.t + 0.5 * self.ax * self.t**2
        self.sy = self.uy * self.t + 0.5 * self.ay * self.t**2
            #IMPORTANT: we are calculating from the launch point every frame, rather than adding small increments for each frame

        self.x = self._launch_x + self.sx * PIXELS_PER_METER #convert from meters to pixels
        self.y = self._launch_y + self.sy * PIXELS_PER_METER

    def bounce(self, ground_y_px, restitution = 0.6):
        #i put the restituion at .6 because it both looks good and seems logical, a bean bag is about 0.2 and a tennis ball is 0.75
        self.y = float(ground_y_px) # make the can be on the ground, not fall through
            
        new_vy = -self.vy * restitution # flip vertical velocity

        if abs(new_vy) < 0.3:
            self.in_flight = False # if the bounce is really tiny, consider it at "rest"
            self.grounded = True
            self.vy = 0.0
            self.vx = 0.0
            return
        self.release(vx_ms = self.vx, vy_ms = new_vy) #relaunch with the new velocities


def run_physics():
    pass

if __name__ == "__main__":
    run_physics()

                
        
                