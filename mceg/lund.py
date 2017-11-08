#!/usr/bin/env python

import numpy as np 
import sys

class LundHeader(object):
    
    def __init__(self):
        self.x  = 0
        self.y  = 0
        self.w  = 0
        self.q2 = 0
        self.nu = 0
        
        self.number_particles = 0
        self.number_target_nucleons = 0
        self.number_target_protons = 0
        self.beam_pol = 0
        self.target_pol = 0

    def __str__(self):
        return '%d    %d    %d    %.6f    %.6f    %.6f    %.6f    %.6f    %.6f    %.6f' % (self.number_particles, 
                                                                                           self.number_target_nucleons, 
                                                                                           self.number_target_protons, 
                                                                                           self.beam_pol, self.target_pol, 
                                                                                           self.x, self.y, self.q2, self.w, 
                                                                                           self.nu
                                                                                           )
class LundParticle(object):

    def __init__(self):
        self.index = 0
        self.charge = 0
        self.type = 0
        self.pid = 0
        self.parent_index = 0
        self.daughter_index = 0
        self.px = 0
        self.py = 0
        self.pz = 0
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.energy = 0
        self.mass = 0

    def __str__(self):
        return '%d    %d    %d    %d    %d    %d    %.6f    %.6f    %.6f    %.6f    %.6f    %.6f    %.6f    %.6f' % (self.index,self.charge,
                                                                                                                     self.type, self.pid, 
                                                                                                                     self.parent_index, 
                                                                                                                     self.daughter_index, 
                                                                                                                     self.px, self.py, self.pz, 
                                                                                                                     self.vx, self.vy, self.vz, 
                                                                                                                     self.energy, self.mass
                                                                                                                   )
class LundEvent(object):
    
    def __init__(self):
        self.header = LundHeader() 
        self.particles = []
        
    def add_particle(self, particle):
        particle.index = len(self.particles)
        self.particles.append(particle)
        self.header.number_particles = len(self.particles)

    def __str__(self):
        event_string = self.header.__str__() + '\n'
        
        for particle in self.particles:
            event_string += particle.__str__()
            
        event_string += '\n'
        return event_string


class LundWriter(object):
    
    def __init__(self):
        self.events   = []

    def add_event(self, event):
        self.events.append(event)

    def print_events(self):
        for ev in self.events:
            print(ev)

    def save_events(self, filename):

        try:
            out = open(filename, 'wb')
            for ev in self.events:
                out.write(ev.__str__())
                
            out.close()
        except:
            print('Error opening %s' % filename)
            

if __name__ == '__main__': 
    
    n_events  = 10000
    beam      = 11.0
    theta_min = 10
    theta_max = 30

    p = np.random.uniform(size=n_events)*beam*0.8
    theta = np.random.uniform(size=n_events)*(theta_max-theta_min) + theta_min
    phi = np.random.uniform(size=n_events)*360


    writer = LundWriter() 
    for mag, polar, azym in zip(p, theta, phi):
        ev = LundEvent() 
        part = LundParticle()
        part.px = mag*np.sin(polar*np.pi/180)*np.cos(azym*np.pi/180)
        part.py = mag*np.sin(polar*np.pi/180)*np.sin(azym*np.pi/180)
        part.pz = mag*np.cos(polar*np.pi/180)
        part.vx = np.random.random()
        part.vy = np.random.random()
        part.vz = np.random.random()
        part.energy = mag
        part.mass   = 0.0 
        part.pid    = 11 
        part.charge = -1

        ev.header.nu = beam - mag
        ev.header.q2 = 4*beam*mag*np.sin(polar/2 * np.pi/180)**2
        ev.header.x  = ev.header.q2/(2*0.938*ev.header.nu)
        ev.header.y  = ev.header.nu/beam
        ev.add_particle(part)
        
        writer.add_event(ev)


    writer.save_events('events.lund')
