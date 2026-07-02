735. Asteroid Collision



class Solution:
	def asteroidCollision(self, asteroids: List[int]) -> List[int]:
		stack = []

		for asteroid in asteroids:
			if not stack:
				stack.append(asteroid)
				continue

			# Keep poping previous asteroid
			while stack:
				recent_ast = stack.pop()

				# Check direction
				if recent_ast > 0 and asteroid < 0:
					# Check collision result
					collision_res = recent_ast + asteroid

					if collision_res == 0:
						break
					elif collision_res > 0:
						stack.append(recent_ast)
						break
					elif not stack:
						stack.append(asteroid)
						break
				else:
					stack.append(recent_ast)
					stack.append(asteroid)
					break

		return stack
