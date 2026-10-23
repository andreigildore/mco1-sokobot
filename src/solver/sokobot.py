import time
import heapq



class SokoBot:
    # Manhattan distance of all crates to the nearest target
    def computeHeuristic(self, crates, targets):
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
        crates = set()

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
                    crates.add((r, c))

        start_state = (player, tuple(crates))

        frontier = []
        heapq.heapify(frontier)
        visited = set()

        heuristic_start = self.computeHeuristic(list(crates), list(targets))
        heapq.heappush(frontier, (heuristic_start, start_state, ""))
        visited.add(start_state)

        moves = [('u', -1, 0), ('d', 1, 0), ('l', 0, -1), ('r', 0, 1)]

        while frontier:         # while frontier is not empty
            h, cur_state, path = heapq.heappop(frontier)

            # check if all crates are in target spaces
            if set(cur_state[1]) >= targets:
                return path
            
            for dir_char, dx, dy in moves:
                next_player = (cur_state[0][0] + dx, cur_state[0][1] + dy)

                # skips if the move is invalid due to a wall
                if next_player in walls:
                    continue

                next_crates = (set(cur_state[1])).copy()

                # check if there's crate push interaction
                if next_player in cur_state[1]:
                    crate_target = (next_player[0] + dx, next_player[1] + dy)

                    # block if space behind the crate is a wall/diff crate
                    if crate_target in walls or crate_target in cur_state[1]:
                        continue
                    # move crate
                    next_crates.remove(next_player)
                    next_crates.add(crate_target)

                next_state = (next_player, tuple(next_crates))
                if next_state not in visited:
                    visited.add(next_state)
                    heuristicVal = self.computeHeuristic(list(next_crates), list(targets))
                    heapq.heappush(frontier, (heuristicVal, next_state, path + dir_char))



