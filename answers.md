
# Part C – Short Answer (Reasoning)

**1. If you only had 200 labeled replies, how would you improve the model without collecting thousands more?**  
With a small dataset, use data augmentation (paraphrasing, backtranslation) and leverage pre-trained language models for transfer learning. Also, cross-validation helps maximize performance on limited data.

**2. How would you ensure your reply classifier doesn’t produce biased or unsafe outputs in production?**  
Perform bias audits, implement rule-based filters for unsafe content, and monitor predictions with human-in-the-loop reviews to reduce harmful outputs.

**3. Suppose you want to generate personalized cold email openers using an LLM. What prompt design strategies would you use to keep outputs relevant and non-generic?**  
Include recipient context (role, company, interests), provide high-quality examples in the prompt, and instruct the model to avoid generic phrasing for more relevant outputs.
