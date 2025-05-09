diseases_data = [
    # 1. Apple Diseases
    {
        "class_name": "Apple___Apple_scab",
        "description": "Fungal disease caused by Venturia inaequalis, common in humid climates.",
        "symptoms": "Olive-green to black spots on leaves, cracked and deformed fruits.",
        "treatment": "Apply sulfur or copper-based fungicides. Remove infected leaves.",
        "prevention": "Prune for air circulation. Avoid overhead watering.",
        "note": "Severe infections can lead to 50% yield loss."
    },
    {
        "class_name": "Apple___Black_rot",
        "description": "Fungal disease (Botryosphaeria obtusa) affecting fruits, leaves, and branches.",
        "symptoms": "Brown spots with concentric rings, black mummified fruits.",
        "treatment": "Remove infected parts. Use captan or thiophanate-methyl fungicides.",
        "prevention": "Disinfect pruning tools. Avoid tree wounds.",
        "note": "Spreads through rain splashes."
    },
    {
        "class_name": "Apple___Cedar_apple_rust",
        "description": "Fungus (Gymnosporangium juniperi-virginianae) requiring juniper as a secondary host.",
        "symptoms": "Yellow-orange leaf spots, horn-like growths underneath leaves.",
        "treatment": "Apply triazole fungicides in early spring.",
        "prevention": "Remove nearby juniper plants.",
        "note": "Lifecycle involves two host plants."
    },
    {
        "class_name": "Apple___healthy",
        "description": "Healthy apple tree with no signs of disease.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Regular monitoring, proper fertilization.",
        "note": "Maintain soil pH between 6.0-7.0."
    },

    # 2. Blueberry
    {
        "class_name": "Blueberry___healthy",
        "description": "Healthy blueberry plant.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Use acidic soil (pH 4.5-5.5). Mulch with pine bark.",
        "note": "Susceptible to root rot in waterlogged soils."
    },

    # 3. Cherry
    {
        "class_name": "Cherry_(including_sour)___Powdery_mildew",
        "description": "Fungal disease (Podosphaera clandestina) forming white powdery patches.",
        "symptoms": "White fuzzy growth on leaves, distorted shoots.",
        "treatment": "Spray sulfur or neem oil.",
        "prevention": "Avoid excess nitrogen. Space plants for airflow.",
        "note": "Worse in cool, humid nights."
    },
    {
        "class_name": "Cherry_(including_sour)___healthy",
        "description": "Healthy cherry tree.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Prune annually to prevent overcrowding.",
        "note": "Watch for aphid infestations."
    },

    # 4. Corn (Maize)
    {
        "class_name": "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
        "description": "Fungal disease (Cercospora zeae-maydis) causing gray-brown lesions.",
        "symptoms": "Rectangular gray-brown spots on leaves.",
        "treatment": "Apply strobilurin fungicides.",
        "prevention": "Rotate crops. Bury crop residues.",
        "note": "Can reduce yields by 30-50%."
    },
    {
        "class_name": "Corn_(maize)___Common_rust_",
        "description": "Fungus (Puccinia sorghi) producing rusty pustules.",
        "symptoms": "Orange-red pustules on leaves.",
        "treatment": "Fungicides (azoxystrobin).",
        "prevention": "Plant resistant hybrids.",
        "note": "Favored by dew and mild temperatures."
    },
    {
        "class_name": "Corn_(maize)___Northern_Leaf_Blight",
        "description": "Fungus (Exserohilum turcicum) causing long, tan lesions.",
        "symptoms": "Cigar-shaped tan spots with dark borders.",
        "treatment": "Chlorothalonil or mancozeb applications.",
        "prevention": "Avoid continuous corn planting.",
        "note": "Severe in wet, humid conditions."
    },
    {
        "class_name": "Corn_(maize)___healthy",
        "description": "Healthy corn plant.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Balanced nitrogen fertilization.",
        "note": "Requires full sun and well-drained soil."
    },

    # 5. Grape
    {
        "class_name": "Grape___Black_rot",
        "description": "Fungus (Guignardia bidwellii) causing fruit rot.",
        "symptoms": "Brown circular leaf spots, black shriveled berries.",
        "treatment": "Apply mancozeb during early season.",
        "prevention": "Train vines for airflow. Remove mummified fruits.",
        "note": "Devastating in warm, wet climates."
    },
    {
        "class_name": "Grape___Esca_(Black_Measles)",
        "description": "Complex disease caused by multiple fungi.",
        "symptoms": "Tiger-striped leaves, white rot in wood.",
        "treatment": "No cure. Remove infected vines.",
        "prevention": "Avoid pruning wounds during rainy periods.",
        "note": "Chronic disease in older vineyards."
    },
    {
        "class_name": "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
        "description": "Fungus (Isariopsis griseola) attacking leaves.",
        "symptoms": "Angular brown spots with yellow halos.",
        "treatment": "Copper-based fungicides.",
        "prevention": "Remove fallen leaves.",
        "note": "Common in tropical regions."
    },
    {
        "class_name": "Grape___healthy",
        "description": "Healthy grapevine.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Annual pruning. Monitor for pests.",
        "note": "Requires well-drained soil."
    },

    # ... (Continuez avec les autres classes de la même manière)
    # 6. Orange
    {
        "class_name": "Orange___Haunglongbing_(Citrus_greening)",
        "description": "Bacterial disease (Candidatus Liberibacter) spread by psyllids.",
        "symptoms": "Yellow shoots, lopsided bitter fruits.",
        "treatment": "No cure. Remove infected trees.",
        "prevention": "Control psyllids with insecticides.",
        "note": "Most destructive citrus disease worldwide."
    },

    # 7. Peach
    {
        "class_name": "Peach___Bacterial_spot",
        "description": "Bacterium (Xanthomonas arboricola) causing leaf and fruit spots.",
        "symptoms": "Dark angular leaf spots, cracked fruits.",
        "treatment": "Copper sprays during dormancy.",
        "prevention": "Plant resistant varieties (e.g., 'Redhaven').",
        "note": "Worse in windy, rainy weather."
    },
    {
        "class_name": "Peach___healthy",
        "description": "Healthy peach tree.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Thin fruits to improve size.",
        "note": "Requires winter chilling hours."
    },

    # 8. Pepper, Bell
    {
        "class_name": "Pepper,_bell___Bacterial_spot",
        "description": "Bacterium (Xanthomonas spp.) causing leaf and fruit lesions.",
        "symptoms": "Water-soaked spots turning brown, defoliation.",
        "treatment": "Copper sprays + mancozeb.",
        "prevention": "Use disease-free seeds.",
        "note": "Spread by splashing water."
    },
    {
        "class_name": "Pepper,_bell___healthy",
        "description": "Healthy bell pepper plant.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Avoid overhead irrigation.",
        "note": "Prefers warm temperatures."
    },

    # 9. Potato
    {
        "class_name": "Potato___Early_blight",
        "description": "Fungus (Alternaria solani) causing concentric leaf spots.",
        "symptoms": "Bull's-eye patterned lesions, yellowing leaves.",
        "treatment": "Chlorothalonil or mancozeb.",
        "prevention": "Rotate with non-solanaceous crops.",
        "note": "Accelerated by nitrogen deficiency."
    },
    {
        "class_name": "Potato___Late_blight",
        "description": "Oomycete (Phytophthora infestans) famous for Irish Famine.",
        "symptoms": "Water-soaked lesions, white mold under leaves.",
        "treatment": "Metalaxyl or fosetyl-Al fungicides.",
        "prevention": "Destroy cull piles. Plant resistant varieties.",
        "note": "Devastating in cool, wet weather."
    },
    {
        "class_name": "Potato___healthy",
        "description": "Healthy potato plant.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Hill soil around stems.",
        "note": "Sensitive to frost."
    },

    # 10. Raspberry
    {
        "class_name": "Raspberry___healthy",
        "description": "Healthy raspberry plant.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Prune old canes after fruiting.",
        "note": "Prefers slightly acidic soil."
    },

    # 11. Soybean
    {
        "class_name": "Soybean___healthy",
        "description": "Healthy soybean plant.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Inoculate seeds with rhizobia.",
        "note": "Fixates atmospheric nitrogen."
    },

    # 12. Squash
    {
        "class_name": "Squash___Powdery_mildew",
        "description": "Fungus (Podosphaera xanthii) forming white powder on leaves.",
        "symptoms": "White patches, premature leaf death.",
        "treatment": "Baking soda spray (1 tbsp/gallon water).",
        "prevention": "Plant resistant varieties (e.g., 'Dunja').",
        "note": "Worse in dry, shady conditions."
    },

    # 13. Strawberry
    {
        "class_name": "Strawberry___Leaf_scorch",
        "description": "Fungus (Diplocarpon earliana) causing leaf browning.",
        "symptoms": "Purple-brown leaf spots, scorched appearance.",
        "treatment": "Remove infected leaves. Apply fungicides.",
        "prevention": "Space plants for airflow.",
        "note": "Overwinters in dead leaves."
    },
    {
        "class_name": "Strawberry___healthy",
        "description": "Healthy strawberry plant.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Renew beds every 3-4 years.",
        "note": "Mulch with straw to suppress weeds."
    },

    # 14. Tomato
    {
        "class_name": "Tomato___Bacterial_spot",
        "description": "Bacterium (Xanthomonas spp.) causing leaf and fruit spots.",
        "symptoms": "Small water-soaked spots with yellow halos.",
        "treatment": "Copper sprays + streptomycin.",
        "prevention": "Use pathogen-free seeds.",
        "note": "Spread by handling wet plants."
    },
    {
        "class_name": "Tomato___Early_blight",
        "description": "Fungus (Alternaria solani) affecting leaves and stems.",
        "symptoms": "Concentric rings on lower leaves, defoliation.",
        "treatment": "Chlorothalonil or copper fungicides.",
        "prevention": "Stake plants for air circulation.",
        "note": "Common in humid climates."
    },
    {
        "class_name": "Tomato___Late_blight",
        "description": "Oomycete (Phytophthora infestans) causing rapid plant collapse.",
        "symptoms": "Greasy gray-green lesions, white mold undersides.",
        "treatment": "Metalaxyl before infection.",
        "prevention": "Avoid overhead watering.",
        "note": "Same pathogen as potato late blight."
    },
    {
        "class_name": "Tomato___Leaf_Mold",
        "description": "Fungus (Passalora fulva) thriving in high humidity.",
        "symptoms": "Yellow upper leaf surfaces, purple-gray mold underneath.",
        "treatment": "Chlorothalonil or potassium bicarbonate.",
        "prevention": "Reduce greenhouse humidity.",
        "note": "Common in enclosed growing spaces."
    },
    {
        "class_name": "Tomato___Septoria_leaf_spot",
        "description": "Fungus (Septoria lycopersici) attacking lower leaves.",
        "symptoms": "Small circular spots with dark margins.",
        "treatment": "Remove infected leaves. Apply copper.",
        "prevention": "Mulch to prevent soil splashing.",
        "note": "Spreads rapidly in wet weather."
    },
    {
        "class_name": "Tomato___Spider_mites Two-spotted_spider_mite",
        "description": "Arachnid (Tetranychus urticae) sucking plant sap.",
        "symptoms": "Fine webbing, stippled yellow leaves.",
        "treatment": "Spray with neem oil or insecticidal soap.",
        "prevention": "Increase humidity. Introduce predatory mites.",
        "note": "Worse in hot, dry conditions."
    },
    {
        "class_name": "Tomato___Target_Spot",
        "description": "Fungus (Corynespora cassiicola) causing bull's-eye lesions.",
        "symptoms": "Brown spots with concentric rings, leaf drop.",
        "treatment": "Chlorothalonil or mancozeb.",
        "prevention": "Avoid dense planting.",
        "note": "Common in tropical regions."
    },
    {
        "class_name": "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
        "description": "Virus (TYLCV) transmitted by whiteflies.",
        "symptoms": "Upward leaf curling, stunted growth.",
        "treatment": "No cure. Remove infected plants.",
        "prevention": "Control whiteflies with reflective mulch.",
        "note": "Resistant varieties available (e.g., 'Tygress')."
    },
    {
        "class_name": "Tomato___Tomato_mosaic_virus",
        "description": "Virus (ToMV) causing mottled leaves.",
        "symptoms": "Mosaic patterns, distorted growth.",
        "treatment": "No cure. Destroy infected plants.",
        "prevention": "Disinfect tools. Avoid smoking near plants.",
        "note": "Persists in soil debris."
    },
    {
        "class_name": "Tomato___healthy",
        "description": "Healthy tomato plant.",
        "symptoms": "None.",
        "treatment": "None.",
        "prevention": "Rotate crops yearly.",
        "note": "Requires full sun (6+ hours daily)."
    }
]