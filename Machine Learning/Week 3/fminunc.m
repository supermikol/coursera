function [jVal, grad] = costFunction(theta)
jVal = theta' * (ones(size(theta,1),1)*5);
grad = zeros(2,1) .* (2 * (theta - 5));