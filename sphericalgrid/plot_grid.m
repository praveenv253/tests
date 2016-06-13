function plot_grid(num_points)
	%% Plot a spherical grid with the given number of points

	filename = sprintf('points-%s.out', num2str(num_points));
	b = dlmread(filename);

	%t = cellstr(num2str(b(:, 1) + 1));
	%dx = 0.03;
	%dy = 0.03;
	%dz = 0.03;
	%text(b(:, 3) + dx, b(:, 4) + dy, b(:, 5) + dz, t);

	% Plot grid
	scatter3(b(:, 3), b(:, 4), b(:, 5), 15, 'k', 'filled');
	hold on;

	% Underlying sphere
	res = 201;
	phi = linspace(0, 2 * pi, res);
	theta = linspace(0, pi, ceil(res/2));
	[Phi, Theta] = meshgrid(phi, theta);

	r = 0.98;
	X = r .* sin(Theta) .* cos(Phi);
	Y = r .* sin(Theta) .* sin(Phi);
	Z = r .* cos(Theta);

	surf(X, Y, Z, 0.8 * ones(size(X)));
	colormap(gray);
	caxis([0, 1]);
	shading interp;
	set(gca, 'Color', 'none');
	daspect([1, 1, 1]);
	axis tight;
	view([70, 25]);
	axis off;
end
