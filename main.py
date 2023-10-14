from settings import * 
import moderngl as mgl
import pygame as pg
import sys

class VoxelEngine:
    def __init__(self) -> None:
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3) #Max version
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3) #Min version
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE) #Avoid using deprecated functions
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24) #24 bits to the depth buffer
        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context() #Create context
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = "auto" #Automatic garbage collector
        
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0
        self.is_running = True
    
    def update(self):
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001 #Time in seconds
        pg.display.set_caption(f"{self.clock.get_fps() :.0f}") #Show fps
    
    def render(self):
        self.ctx.clear(color=BG_COLOR) #Clear buffer
        pg.display.flip() #Flip to display new frame
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
    
    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit(0)
    
if __name__ == "__main__":
    app = VoxelEngine()
    app.run()