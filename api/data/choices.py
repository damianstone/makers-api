from model_utils import Choices

INDUSTRY_CHOICES = Choices(
    ("agriculture", "Agriculture"),
    ("construction", "Construction"),
    ("education", "Education"),
    ("energy", "Energy"),
    ("engineering", "Engineering"),
    ("environment", "Environment"),
    ("finance", "Finance"),
    ("food-beverages", "Food & Beverages"),
    ("healthcare", "Healthcare"),
    ("hospitality", "Hospitality"),
    ("information-technology", "Information Technology"),
    ("internet", "Internet"),
    ("legal", "Legal"),
    ("logistics", "Logistics"),
    ("manufacturing", "Manufacturing"),
    ("media", "Media"),
    ("mining", "Mining"),
    ("music", "Music"),
    ("pharmaceuticals", "Pharmaceuticals"),
    ("public-administration", "Public Administration"),
    ("real-estate", "Real Estate"),
    ("recreation", "Recreation"),
    ("retail", "Retail"),
    ("science", "Science"),
    ("services", "Services"),
    ("technology", "Technology"),
    ("telecommunications", "Telecommunications"),
    ("textiles", "Textiles"),
    ("transportation", "Transportation"),
    ("travel", "Travel"),
)

INTEREST_CHOICES = Choices(
    ("business-development", "Business Development"),
    ("collaboration", "Collaboration"),
    ("contracting-services", "Contracting Services"),
    ("distribution", "Distribution"),
    ("equity-investment", "Equity Investment"),
    ("franchising", "Franchising"),
    ("joint-venture", "Joint Venture"),
    ("licensing", "Licensing"),
    ("mergers-acquisitions", "Mergers & Acquisitions"),
    ("outsourcing", "Outsourcing"),
    ("product-development", "Product Development"),
    ("research-development", "Research & Development"),
    ("sales-marketing", "Sales & Marketing"),
    ("sponsorship", "Sponsorship"),
    ("strategic-alliance", "Strategic Alliance"),
    ("supply-chain", "Supply Chain"),
    ("technology-transfer", "Technology Transfer"),
    ("venture-capital", "Venture Capital"),
    ("white-labeling", "White Labeling"),
)

TYPE_CHOICES = Choices(("startup", "Startup"), ("corporation", "Corporation"))
