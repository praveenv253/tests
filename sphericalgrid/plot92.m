b = dlmread('points-92.out');
scatter3(b(:, 3), b(:, 4), b(:, 5), 30, b(:, 5), 'filled');
hold on;
t = cellstr(num2str(b(:, 1) + 1));
dx = 0.03;
dy = 0.03;
dz = 0.03;
text(b(:, 3) + dx, b(:, 4) + dy, b(:, 5) + dz, t);