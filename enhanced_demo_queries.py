#!/usr/bin/env python3
"""
Enhanced Demo Queries for Project Samarth
Comprehensive questions designed to showcase the app's multi-state comparison capabilities
"""

def get_enhanced_demo_queries():
    """
    Return comprehensive demo queries that work perfectly with Project Samarth's capabilities
    """
    
    queries = {
        "Multi-State Rainfall & Crop Comparison": [
            # Question 1: Multi-state rainfall comparison with crop analysis
            """Compare the average annual rainfall in Karnataka and Tamil Nadu for the last 5 available years. 
            In parallel, list the top 5 most produced crops (by volume) in each of those states during the same period, 
            citing all data sources.""",
            
            # Question 2: District-level production comparison
            """Identify the district in Punjab with the highest production of wheat in the most recent year available 
            and compare that with the district with the lowest production of wheat in Rajasthan. 
            Include production volumes, area under cultivation, and productivity per hectare.""",
            
            # Question 3: Regional crop trend analysis with climate correlation
            """Analyze the production trend of rice cultivation in South India (Karnataka, Tamil Nadu, Andhra Pradesh, Telangana) 
            over the last decade. Correlate this trend with the corresponding rainfall data for the same period and provide 
            a summary of the apparent climate impact on rice productivity.""",
            
            # Question 4: Policy recommendation with data backing
            """A policy advisor is proposing a scheme to promote drought-resistant crops (like millets, bajra) over 
            water-intensive crops (like sugarcane, rice) in Maharashtra. Based on historical data from the last 5 years, 
            what are the three most compelling data-backed arguments to support this policy? Your answer must synthesize 
            data from both climate and agricultural sources."""
        ],
        
        "Ready-to-Use Queries for Your App": [
            # Framed for immediate use in your Project Samarth app
            "Compare the average annual rainfall in Karnataka and Tamil Nadu - show monsoon patterns and agricultural impact",
            
            "List the top 5 most produced crops in Punjab vs Maharashtra for 2020-2022 period with production volumes",
            
            "Identify the highest wheat producing district in Punjab and compare with lowest wheat production in Rajasthan",
            
            "Analyze rice production trends in South India over the last decade and correlate with rainfall patterns",
            
            "Show drought-resistant vs water-intensive crop analysis for Maharashtra with climate data support",
            
            "Compare sugarcane cultivation: Maharashtra vs Uttar Pradesh - production, climate, and sustainability analysis",
            
            "Multi-state cotton analysis: Gujarat vs Telangana vs Maharashtra with climate factors",
            
            "Monsoon dependency analysis: Punjab vs Tamil Nadu farming systems and irrigation requirements",
            
            "Regional crop diversification patterns: North India vs South India agricultural strategies",
            
            "Climate resilience assessment: Which states are best positioned for sustainable agriculture?"
        ],
        
        "Specific Demo Scenarios": [
            # Scenario 1: Agricultural Policy Advisor
            {
                "role": "Agricultural Policy Advisor",
                "context": "Developing water conservation policies",
                "questions": [
                    "Compare water-intensive crops (rice, sugarcane) vs drought-resistant crops (millets, bajra) across Maharashtra, Karnataka, and Gujarat",
                    "Which districts in these states should prioritize crop diversification based on rainfall patterns?",
                    "What are the economic and environmental trade-offs of promoting drought-resistant crops?"
                ]
            },
            
            # Scenario 2: Climate Researcher
            {
                "role": "Climate Researcher", 
                "context": "Studying monsoon impact on agriculture",
                "questions": [
                    "How do Southwest vs Northeast monsoon patterns affect crop choices in Tamil Nadu vs Kerala?",
                    "Compare rainfall variability and agricultural adaptation strategies in Punjab vs Rajasthan",
                    "Which crops show strongest correlation with monsoon rainfall across different states?"
                ]
            },
            
            # Scenario 3: Farmer Advisory
            {
                "role": "Agricultural Extension Officer",
                "context": "Advising farmers on optimal crop selection",
                "questions": [
                    "For a farmer in drought-prone regions of Maharashtra, what crops offer best climate resilience?",
                    "Compare cotton vs soybean profitability and climate suitability in Gujarat vs Madhya Pradesh",
                    "Which states have successfully diversified from water-intensive to climate-resilient crops?"
                ]
            }
        ],
        
        "Quick Test Queries": [
            # Simple queries to test core functionality
            "Compare rice production in Punjab vs Tamil Nadu",
            "Show rainfall patterns in Karnataka vs Maharashtra", 
            "Analyze sugarcane cultivation across states",
            "Which crops are best suited for low rainfall regions?",
            "Compare monsoon dependency: North vs South India",
            "Show top wheat producing districts in India",
            "Climate impact on cotton cultivation analysis",
            "Drought-resistant crop recommendations for Maharashtra",
            "Multi-state agricultural productivity comparison",
            "Seasonal cropping patterns across Indian states"
        ]
    }
    
    return queries

def format_for_app_demo():
    """
    Format queries specifically for Project Samarth app demonstration
    """
    
    print("🌾 PROJECT SAMARTH - ENHANCED DEMO QUERIES")
    print("=" * 60)
    
    queries = get_enhanced_demo_queries()
    
    print("\n🎯 COPY-PASTE READY QUERIES FOR YOUR APP:")
    print("-" * 50)
    
    for i, query in enumerate(queries["Ready-to-Use Queries for Your App"], 1):
        print(f"\n{i:2d}. {query}")
    
    print("\n\n🚀 QUICK TEST QUERIES (Start with these):")
    print("-" * 50)
    
    for i, query in enumerate(queries["Quick Test Queries"][:5], 1):
        print(f"\n{i}. {query}")
    
    print("\n\n💡 COMPREHENSIVE ANALYSIS QUERIES:")
    print("-" * 50)
    
    for i, query in enumerate(queries["Multi-State Rainfall & Crop Comparison"], 1):
        print(f"\n{i}. {query}")
    
    print("\n\n🎭 ROLE-BASED DEMO SCENARIOS:")
    print("-" * 50)
    
    for scenario in queries["Specific Demo Scenarios"]:
        print(f"\n👤 {scenario['role']} - {scenario['context']}")
        for j, q in enumerate(scenario['questions'], 1):
            print(f"   {j}. {q}")
    
    print("\n\n✅ YOUR APP CAPABILITIES SHOWCASED:")
    print("-" * 50)
    print("✅ Multi-state agricultural comparisons")
    print("✅ Climate-agriculture correlation analysis")
    print("✅ District-level production insights")
    print("✅ Crop trend analysis over time")
    print("✅ Policy recommendation support")
    print("✅ Real-time data synthesis")
    print("✅ Interactive agricultural intelligence")
    
    print(f"\n🎉 Total demo queries available: {sum(len(v) if isinstance(v, list) else len(v) for v in queries.values())}")
    print("\n💻 Ready to demonstrate Project Samarth's comprehensive capabilities!")

if __name__ == "__main__":
    format_for_app_demo()