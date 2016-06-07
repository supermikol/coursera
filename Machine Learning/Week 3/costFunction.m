function [jVal, gradient] = costFunction(theta)

jVal = sum((theta-5).^2);
gradient = 2 * (theta - 5); %compute derivative of cost w/ respect to theta. This is delta