import time
import heapq



class SokoBot:
    # Manhattan distance of all crates to the nearest target
    def computeHeuristic(crates, targets):
        total_distance = 0
        for c in crates:
            min_distance = min(abs(c[0] - t[0]) + abs(c[1] - t[1]) for t in targets)
            total_distance += min_distance
        return total_distance

    def solveSokobanPuzzle(self, width, height, mapData, itemsData):
        # YOU NEED TO REWRITE THE IMPLEMENTATION OF THIS METHOD TO MAKE THE BOT SMARTER
        # Default stupid behavior: Think (sleep) for 3 seconds, and then return a
        # sequence
        # that just moves left and right repeatedly.
        
        walls = set()
        targets = set()
        player = None
        crates = []

        # stores the coordinates of the targets
        for r in range(height):
            for c in range(width):
                if mapData[r][c] == '.':
                    targets.add((r, c))
                elif mapData[r][c] == '#':
                    walls.add((r, c))
        
        # store the coordinates of the player and crates
        for r in range(height):
            for c in range(width):
                if itemsData[r][c] == '@':
                    player = (r, c)
                elif itemsData[r][c] == '$':
                    crates.append((r, c))

        start_state = (player, tuple(sorted(crates)), "")

        frontier = []
        heapq.heapify(frontier)
        visited = set()

        hueristic_start = self.computeHeuristic(crates, list(targets))
        heapq.heappush(frontier, (hueristic_start, start_state))
        visited.add(start_state)

        moves = [('u', 0, -1), ('d', 0, 1), ('l', -1, 0), ('r', 1, 0)]

        while frontier:         # while frontier is not empty 
            cur_state = heapq.heappop(frontier)

            # check if all crates are in target spaces
            if cur_state[1] in targets:
                return cur_state[2]
            
            for dir_char, dx, dy in moves:
                next_player 

        return "rrrddlllrrruullldurrrddlludrruuldllur"
