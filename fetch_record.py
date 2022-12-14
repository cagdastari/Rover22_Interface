#!/usr/bin/env python33
import sqlite3
from rock_info import rock

class fetcher:
    def __init__(self):
        conn=sqlite3.connect('/home/cagdas/interface_ws/src/-22-Rover-Interface-1.0/rover_ui/nodes/rocks.db')
        
        c=conn.cursor()
        c.execute("SELECT r.name,r.class,r.description FROM rocks as r")

        self.list=[]
        rocks=c.fetchall()
        for x in rocks:
            self.list.append(rock(x[0],x[1],x[2]))

        conn.commit()
        conn.close()


    def fetch(self):
        return self.list
