.PHONY: clean All

All:
	@echo "----------Building project:[ Naive_Bayes - Debug ]----------"
	@"$(MAKE)" -f  "Naive_Bayes.mk"
clean:
	@echo "----------Cleaning project:[ Naive_Bayes - Debug ]----------"
	@"$(MAKE)" -f  "Naive_Bayes.mk" clean
