            
            # depending on the area clicked on, run different delta-variables
            if self.edgeloc != "": # edge/center was clicked
                self.mouse_mode = "edge"
            elif x<1 and y<1: # menu was clicked
                self.mouse_mode = "menu"
                
            elif map_visible and x in range(self.res[0]-map_mscreen-map_res[0], win_res[0]-map_mscreen) and y in range(map_mscreen, map_mscreen+map_res[1]): # click to map
                self.mouse_mode = "map" # move map
            elif x in range(ui_pos[0], ui_pos[0] + ui_res[0]) and y in range(ui_pos[1], ui_pos[1] + ui_res[1]): # menu was clicked
                print("Menu clicked")
            elif self.mouse_mode == "mark": # menu was clicked
                self.mouse_mode = "markpaint"
            elif self.mouse_mode == "ocr": # menu was clicked
                self.mouse_mode = "ocrpaint"
            else:
                if self.mouse_mode == "":
                    self.mouse_mode = "pan"

            # ~ if (x in range(win_res[0]-50,win_res[0]) and y in range(win_res[1]-50,win_res[1])) and (not fullscreen) and (not reshape):
                # ~ reshape = True
                # ~ reshape_start = (x, y)
                # ~ win_delta = (0, 0)
           
            # clicked in reshape-area
            # ~ if edge_move:
                # ~ window['pos'] = (x - edge_old[0], y- edge_old[1])
                
                # ~ print(window['pos'])
                
            # ~ if reshape:
                # ~ win_delta = (x - reshape_start[0], y - reshape_start[1])


                
