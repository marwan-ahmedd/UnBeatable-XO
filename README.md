<!DOCTYPE html>
<html>
<head>
	<title>Unbeatable XO Minimax Repository</title>
	<link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="style.css">
</head>
<body>
	<header>
		<h1>Unbeatable XO Minimax Repository</h1>
		<nav>
			<ul>
				<li><a href="#">Home</a></li>
				<li><a href="#">About</a></li>
				<li><a href="#">Documentation</a></li>
				<li><a href="#">Contact</a></li>
			</ul>
		</nav>
	</header>
	<main>
		<section>
			<h2>What is Unbeatable XO Minimax?</h2>
			<p>Unbeatable XO Minimax is a repository that provides an implementation of the minimax algorithm for Tic-Tac-Toe.</p>
		</section>
		<section>
			<h2>How to Use</h2>
			<p>To use the repository, simply clone the code and run it on your local machine.</p>
			<pre><code class="language-python">def minimax(game_state, player):
    if game_is_over(game_state):
        return score(game_state, player)
    if player == MAX_PLAYER:
        best_score = -inf
        for move in possible_moves(game_state):
            new_game_state = make_move(game_state, move, player)
            score = minimax(new_game_state, MIN_PLAYER)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = inf
        for move in possible_moves(game_state):
            new_game_state = make_move(game_state, move, player)
            score = minimax(new_game_state, MAX_PLAYER)
            best_score = min(best_score, score)
        return best_score</code></pre>
		</section>
	</main>
	<footer>
		<p>Copyright &copy; 2023 Unbeatable XO Minimax Repository</p>
	</footer>
</body>
</html>
