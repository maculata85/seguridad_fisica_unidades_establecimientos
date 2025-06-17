# -*- coding: utf-8 -*-
"""
Este archivo contiene la base de datos completa con 350 preguntas y respuestas
para el cuestionario sobre Seguridad Física de las Unidades y Establecimientos de la SEMAR.
"""

BASE_DE_PREGUNTAS = [
    # Bloque 1 de 6: Preguntas 1-50
    {
        "pregunta": "¿Cuál es el propósito principal del manual 'DAM 1.3.4.6 Seguridad Física de las Unidades y Establecimientos de la Secretaría de Marina Armada de México'?",
        "opciones": ["Establecer directrices para el personal de infantería de marina.", "Orientar y normar la actuación del personal para el mantenimiento de la seguridad de las Unidades y Establecimientos navales.", "Detallar procedimientos de respuesta ante desastres naturales.", "Describir la organización interna de la Secretaría de Marina."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "¿Qué tipo de recursos busca proteger la seguridad física en las Unidades y Establecimientos navales?",
        "opciones": ["Solo recursos materiales y financieros.", "Exclusivamente recursos humanos.", "Recursos humanos, materiales y financieros.", "Únicamente instalaciones navales."],
        "respuesta_correcta": 2,
        "dificultad": "facil",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "¿Cuántos capítulos expone el modelo doctrinario para la Seguridad Física en las Unidades y Establecimientos de la Secretaría de Marina - Armada de México?",
        "opciones": ["Dos", "Tres", "Cuatro", "Cinco"],
        "respuesta_correcta": 2,
        "dificultad": "facil",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "Según el Prefacio, ¿qué temas importantes en materia de seguridad abarca el modelo doctrinario?",
        "opciones": ["Seguridad física, amenazas y vulnerabilidades, protección física y cultura de seguridad física.", "Solo amenazas y vulnerabilidades.", "Exclusivamente protección física.", "Planes de contingencia y respuesta a emergencias."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "¿Qué valor adquiere el personal naval al conocer el modelo doctrinario?",
        "opciones": ["Conocimiento para la administración financiera.", "Conocimiento que norma las características, procedimientos, equipo y material empleado para la seguridad de las instalaciones navales.", "Conocimiento sobre estrategias de ataque.", "Conocimiento para la selección de personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "¿Qué documento fue el resultado del trabajo de actualización del DAM 1.3.3.5.7 'Modelo de Seguridad en las Instalaciones de Infantería de Marina'?",
        "opciones": ["El presente documento (DAM 1.3.4.6).", "Un manual de operación naval.", "Una guía de entrenamiento físico.", "Un protocolo de comunicación."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "¿A quién se recomienda proponer cambios o adiciones para mejorar la calidad del modelo doctrinario en ediciones posteriores?",
        "opciones": ["Al personal de seguridad de las unidades.", "A la Dirección del Centro de Estudios Superiores Navales.", "A los lectores del documento.", "Al Comandante de cada unidad."],
        "respuesta_correcta": 2,
        "dificultad": "facil",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "Para asegurar la comprensión y mejor valoración de una propuesta de cambio, ¿qué se debe citar específicamente?",
        "opciones": ["La experiencia personal del proponente.", "El término y concepto cuyo cambio se recomienda y las razones que lo fundamenten.", "Solo el número de página donde se encuentra el concepto.", "La opinión de otros miembros del personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "¿Cuál es la misión de la Secretaría de Marina - Armada de México, según la introducción?",
        "opciones": ["Emplear el Poder Naval de la Federación para la defensa exterior y coadyuvar en la seguridad interior del país.", "Realizar operaciones de rescate en alta mar.", "Gestionar los recursos financieros del país.", "Supervisar el comercio marítimo internacional."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Introducción"
    },
    {
        "pregunta": "¿Por qué la seguridad física de las Unidades y Establecimientos ha cobrado mayor relevancia a raíz de los hechos suscitados el 1 de enero de 1994 en Chiapas?",
        "opciones": ["Por la participación de las fuerzas armadas en eventos deportivos.", "Debido al levantamiento armado del EZLN y ataques directos a instalaciones del Ejército Mexicano, y la participación actual contra la delincuencia organizada.", "Por la necesidad de modernizar los equipos de comunicación.", "A causa de la expansión de la infraestructura naval."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Introducción"
    },
    {
        "pregunta": "¿Qué tipo de eventos han revelado riesgos y vulnerabilidades en los sistemas de seguridad de las instalaciones navales, según el documento?",
        "opciones": ["Conflictos laborales internos.", "Ataques directos por parte de la delincuencia organizada, robo y/o pérdida de material clasificado y fuga de información.", "Desastres naturales sin impacto en la seguridad.", "Cambios en la política internacional."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Introducción"
    },
    {
        "pregunta": "¿Qué ha emitido el Alto Mando de la Secretaría de Marina Armada de México ante la situación de riesgos y vulnerabilidades?",
        "opciones": ["Nuevos reglamentos de vestimenta.", "Instrucciones y directivas para incrementar las medidas de seguridad en los recursos humanos, materiales y financieros.", "Un plan de expansión de personal.", "Un programa de intercambio cultural."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Introducción"
    },
    {
        "pregunta": "¿Cuál es el objetivo de este trabajo (el manual) en relación con el personal de la Secretaría de Marina - Armada de México?",
        "opciones": ["Capacitar en el uso de armamento moderno.", "Orientar y normar la actuación del personal para proporcionar la seguridad a las unidades y establecimientos navales.", "Establecer un plan de retiro para el personal.", "Promover la investigación científica marina."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Introducción"
    },
    {
        "pregunta": "¿Qué se establecen en el documento para garantizar la seguridad del personal y de las instalaciones navales?",
        "opciones": ["Solamente nuevos equipos de vigilancia.", "Conceptos, principios, medidas y procedimientos para conocimiento y aplicación de todo el personal naval.", "Un sistema de recompensas por buena conducta.", "Horarios de trabajo flexibles."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Introducción"
    },
    {
        "pregunta": "¿Qué son las medidas de seguridad física según el Concepto de Seguridad Física?",
        "opciones": ["Acciones para el bienestar del personal.", "Medidas que se adoptan para evitar lesión o pérdidas de vidas, daño, desorganización, destrucción de bienes muebles e inmuebles de la nación, y hacer lo necesario para que estos existan, se desarrollen y cumplan los propósitos fijados.", "Estrategias para la defensa militar.", "Protocolos para la adquisición de nuevos materiales."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Cuáles son algunos de los factores que afectan la seguridad física de las unidades y establecimientos de la Secretaría de Marina Armada de México?",
        "opciones": ["El color de la pintura de las instalaciones y el número de plantas.", "Tamaño y naturaleza, misión, vulnerabilidad, ubicación geográfica, situación económica y política del área, factibilidad de apoyo externo, capacidades propias y del enemigo.", "La cantidad de vehículos y el tipo de armamento.", "Las preferencias alimentarias del personal y el clima."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿En quién recae la responsabilidad de la seguridad de la unidad o establecimiento?",
        "opciones": ["En el personal de guardia.", "En el jefe de seguridad nombrado directamente por el responsable de la instalación.", "En el comandante o director de la unidad o establecimiento.", "En el oficial de vigilancia."],
        "respuesta_correcta": 2,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Quién ejerce la figura de jefe de seguridad en una unidad o establecimiento naval?",
        "opciones": ["El oficial de día.", "El personal de tropa.", "Por nombramiento directo del responsable de la instalación, siendo los elementos idóneos los jefes de la sección tercera, jefes de sección de operaciones e información o jefes administrativos, coordinadores de servicios y mantenimiento.", "El personal de limpieza."],
        "respuesta_correcta": 2,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué incluyen los deberes del jefe de seguridad?",
        "opciones": ["Únicamente la supervisión del personal de guardia.", "Diagnóstico, planeo y ejecución de acciones para la seguridad física.", "La planificación de eventos sociales.", "El manejo de la correspondencia oficial."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Quiénes se encuentran bajo el mando del jefe de seguridad como ejecutantes de la acción planeada?",
        "opciones": ["Solo el oficial de vigilancia.", "El oficial de seguridad de la información (OSI), oficial de vigilancia, oficial de cuartel, oficial de guardia en prevención, oficial de día y todos aquellos elementos con funciones de seguridad en las instalaciones navales.", "El personal administrativo.", "Los proveedores externos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué tipo de servicios de guardia se nombran en la orden general o particular de cada unidad y establecimiento?",
        "opciones": ["Solo servicios de apoyo.", "Servicios de armas y de apoyo.", "Únicamente servicios administrativos.", "Servicios de limpieza."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Cuál es la principal función de la seguridad física según el documento?",
        "opciones": ["La realiza la guardia de apoyo.", "La realiza la guardia en prevención.", "La realiza el oficial de día.", "La realiza el jefe de seguridad."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Cómo se define el riesgo en las unidades y establecimientos navales?",
        "opciones": ["Como la certeza de que no ocurrirá un evento negativo.", "Como la probabilidad de que se produzca un evento y sus consecuencias negativas.", "Como un evento sin impacto significativo.", "Como una oportunidad de mejora."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué factores componen el riesgo?",
        "opciones": ["Solo la amenaza.", "La amenaza y la vulnerabilidad.", "Únicamente la vulnerabilidad.", "El tamaño y la ubicación."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué son los riesgos en las unidades y establecimientos navales?",
        "opciones": ["Condiciones que solo afectan el material.", "Condiciones que pueden dar como resultado la pérdida o daño de recursos humanos, materiales y financieros.", "Factores que siempre mejoran la eficiencia.", "Eventos que solo ocurren en el exterior."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Cómo se clasifican los riesgos según el documento?",
        "opciones": ["Mayores y menores.", "Internos y externos.", "Naturales y Antropogénicos.", "Programados y no programados."],
        "respuesta_correcta": 2,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Cuáles son ejemplos de riesgos naturales mencionados?",
        "opciones": ["Robo de información y ataques armados.", "Terremoto, tsunamis, inundación, incendio, tormenta y temperaturas extremas.", "Descuidos humanos y actos intencionales.", "Fuga de personal y fallos tecnológicos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué son los riesgos antropogénicos?",
        "opciones": ["Consecuencia de fenómenos naturales.", "Descuidos humanos que resultan en daño, pérdida o comprometimiento; y actos intencionales de comisión u omisión contra las unidades y establecimientos navales.", "Eventos climáticos extremos.", "Fallas en el sistema eléctrico."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿De qué dependen las decisiones sobre la seguridad y los medios para lograrla en el planeamiento de seguridad?",
        "opciones": ["Únicamente de la situación económica.", "Del tamaño y naturaleza, misión, vulnerabilidad, ubicación geográfica, situación económica y política del área, factibilidad de apoyo externo, capacidades propias y del enemigo o trasgresor de la ley.", "Solo del número de personal disponible.", "De la antigüedad de las instalaciones."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué son los estudios de estado mayor para analizar la seguridad física de una instalación?",
        "opciones": ["Instrumentos opcionales para el planeamiento.", "Instrumentos indispensables para asegurar un eficiente proceso de planeación y ejecución de las acciones tendientes a garantizar la seguridad de las unidades y establecimientos navales.", "Métodos para la evaluación del personal.", "Herramientas para la contabilidad."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Cuándo es necesario revisar y actualizar la planificación de seguridad física?",
        "opciones": ["Cada cinco años.", "Solo si hay un incidente grave.", "Al existir cambios estructurales o tecnológicos que afecten a la seguridad de las unidades y establecimientos.", "Solo al inicio de un nuevo año fiscal."],
        "respuesta_correcta": 2,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿En qué se dividen los elementos de seguridad física de las unidades y establecimientos navales?",
        "opciones": ["En sistemas y procesos.", "En recursos humanos y materiales.", "En tácticas y estrategias.", "En prevención y respuesta."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué tipo de personal compone los recursos humanos para garantizar la seguridad de las unidades y establecimientos navales?",
        "opciones": ["Personal voluntario.", "Personal capacitado y adiestrado en el manejo de las diferentes situaciones propias de la seguridad física.", "Personal administrativo exclusivamente.", "Personal externo contratado."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Quiénes son algunos de los recursos humanos mencionados para la seguridad?",
        "opciones": ["Cocineros y jardineros.", "Jefe de seguridad, Oficial de Vigilancia, Oficial de Cuartel, Oficial de Día, Guardia en Prevención, Fuerza de Reacción Inmediata y Servicios de Apoyo.", "Médicos y enfermeros.", "Constructores y arquitectos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué son los recursos materiales para la seguridad física?",
        "opciones": ["Aquellos que se emplean para optimizar el trabajo y desempeño del recurso humano encargado de la seguridad física de las unidades y establecimientos navales.", "Los edificios y la infraestructura básica.", "Los uniformes del personal.", "Los vehículos de transporte."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Cuál es la función de la Sala de Guardia y Puestos de Vigilancia?",
        "opciones": ["Almacenar equipo de oficina.", "Son las edificaciones que permiten alojar o establecer al personal de guardia de tal manera que puedan ser empleados de manera inmediata en caso de una situación contingente.", "Realizar reuniones administrativas.", "Exhibir material histórico."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué características se prefieren para las barreras perimétricas?",
        "opciones": ["Sin características especiales.", "Barda o cercado, preferentemente con resguardo de concertina o alambre de púas en la parte superior.", "Barreras de madera simples.", "Muros decorativos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Cuál es la función principal de la iluminación en los linderos de las unidades y establecimientos navales?",
        "opciones": ["Decorar el exterior.", "Mantener una disuasión efectiva eliminando sombras con suficiente potencia y traslapando los campos de iluminación.", "Proporcionar luz para el personal de limpieza.", "Indicar la dirección del viento."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué permiten las señales audibles o sonoras planeadas con anticipación?",
        "opciones": ["Indicar la hora del día.", "Emitir una alerta rápida en caso de situaciones de emergencia.", "Reproducir música ambiental.", "Comunicar mensajes no urgentes."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué incluye el registro y control para la seguridad física?",
        "opciones": ["Identificación del personal naval con credencial de alta seguridad, uso de vehículos oficiales con placas, tarjetones de acceso para vehículos particulares del personal naval, registro de personas y vehículos de proveedores.", "Solo el registro de entrada del personal superior.", "El inventario de suministros de oficina.", "La lista de correos electrónicos."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué debe permitir un sistema y plan de comunicaciones para los elementos de guardia?",
        "opciones": ["Escuchar programas de radio.", "Mantener una intercomunicación eficiente y efectiva en todo momento, ya sea por teléfono, radio o señales a una estación central de control de seguridad y un sistema alterno adecuado.", "Enviar mensajes personales.", "Conectar solo con unidades fuera del establecimiento."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Cómo se definen las amenazas a la seguridad física de las Unidades y Establecimientos Navales?",
        "opciones": ["Como oportunidades de mejora.", "Como fenómenos, sustancias, actitudes humanas o condiciones peligrosas que pueden ocasionar la muerte o lesiones; daños a la propiedad o pérdida de servicios. También acciones reales o percibidas, provocadas por un eventual adversario con intención y capacidad de afectar negativamente intereses propios.", "Como pequeños inconvenientes sin importancia.", "Como eventos planificados para el entrenamiento."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Cómo se define la vulnerabilidad aplicada a unidades y establecimientos navales?",
        "opciones": ["Como la fortaleza del sistema de seguridad.", "Como la facilidad para recibir un daño o perjuicio físico, generalmente por puntos o áreas débiles en el sistema de seguridad física.", "Como la capacidad de resistir cualquier ataque.", "Como la resiliencia del personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Cuáles son algunas de las amenazas comunes a la seguridad física de las unidades y establecimientos navales mencionadas?",
        "opciones": ["Crecimiento económico y estabilidad política.", "Ataques armados del tipo Golpe de Mano, robo de material clasificado, robo hormiga, fuga de información, cooptación e infiltración de personal de la Delincuencia Organizada, intervención de señales, venta de estupefacientes, fenómenos hidrometeorológicos, incendios, enfermedades epidemiológicas.", "Celebraciones y eventos públicos.", "Nuevas tecnologías y avances científicos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Qué tipo de ataques armados se mencionan como amenaza común?",
        "opciones": ["Ataques cibernéticos.", "Ataques del tipo Golpe de Mano.", "Ataques aéreos.", "Ataques psicológicos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "Además del robo de material clasificado, ¿qué otro tipo de robo se menciona como amenaza?",
        "opciones": ["Robo de vehículos.", "Robo de identidad.", "Robo hormiga de productos diversos.", "Robo de armamento pesado."],
        "respuesta_correcta": 2,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Qué fenómenos naturales se consideran amenazas a la seguridad física?",
        "opciones": ["Lluvias ligeras.", "Fenómenos hidrometeorológicos e incendios (también puede ser provocado por el hombre).", "La caída de hojas de los árboles.", "La presencia de animales domésticos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Cuáles son algunas de las vulnerabilidades comunes a la seguridad física en las unidades y establecimientos navales?",
        "opciones": ["Exceso de personal y demasiados recursos.", "Deficiencia de la cultura de prevención y seguridad, apatía para la supervisión de material clasificado, falta de controles y registro de entrada y salida de material, descuido en el manejo de información clasificada, debilidad del sistema de control y confianza institucional, órganos de reclutamiento carentes de plataformas de investigación del personal, pérdida o robo de claves de encriptación o equipos de comunicación, falta de revisiones aleatorias, omisión al seguimiento de fenómenos hidrometeorológicos, ausencia de procedimientos de seguridad contraincendios y falta de controles sanitarios adecuados.", "La construcción de nuevas áreas.", "La modernización de los equipos de comunicación."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Qué tipo de descuido se menciona como vulnerabilidad en el manejo de información?",
        "opciones": ["Descuido en el almacenamiento de documentos.", "Descuido en el manejo de información clasificada.", "Descuido en la distribución de folletos.", "Descuido en la gestión de archivos públicos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Qué se considera una vulnerabilidad relacionada con el personal de reclutamiento?",
        "opciones": ["Órganos de reclutamiento con exceso de personal.", "Órganos de reclutamiento carentes de plataformas de investigación del personal.", "Órganos de reclutamiento con demasiada experiencia.", "Órganos de reclutamiento que solo trabajan en línea."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },

    # Bloque 2 de 6: Preguntas 51-100
    {
        "pregunta": "¿Qué comprende el Concepto de Protección Física?",
        "opciones": ["Solo el mantenimiento de equipos.", "El conjunto de políticas y medidas para mejorar la seguridad física; así como prevenir y controlar los riesgos hacia los recursos humanos, materiales y financieros, haciendo posible que las unidades y establecimientos conserven de manera óptima las capacidades y funciones.", "Únicamente la defensa militar.", "La gestión de recursos humanos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Quiénes dictan las políticas a las que hace referencia la protección física?",
        "opciones": ["El personal de guardia.", "El Alto Mando de la Secretaría de Marina, a través de instrucciones y directivas.", "Los supervisores de seguridad.", "Los jefes administrativos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué ocurre una vez que los Mandos Superiores y Subordinados adecúan las políticas de protección física?",
        "opciones": ["Se descartan por completo.", "Se materializan, considerando los factores de riesgo, implementando las medidas de protección física y supervisando el cumplimiento de las mismas.", "Se envían para revisión externa.", "Se ignoran en la práctica diaria."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué son las Medidas de Protección Física?",
        "opciones": ["Estrategias de comunicación.", "Estructuras y procedimientos que se implementan para minimizar los riesgos a la seguridad física de las unidades y establecimientos navales, como consecuencia del análisis y evaluación de las amenazas y vulnerabilidades.", "Solo los planes de emergencia.", "Las acciones de limpieza de las instalaciones."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué es una de las medidas de protección física mencionadas?",
        "opciones": ["La decoración de interiores.", "La delimitación del lindero de las unidades y establecimientos navales con barreras perimétricas.", "La organización de eventos sociales.", "La compra de nuevos vehículos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se debe identificar y controlar como medida de protección física?",
        "opciones": ["Los puntos de venta de alimentos.", "Los accesos.", "Los lugares de recreación.", "Los espacios de estacionamiento internos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué tipo de instalación se menciona como medida de protección física en relación con la vigilancia?",
        "opciones": ["Instalación de juegos infantiles.", "Instalación de sistema de vigilancia de circuito cerrado.", "Instalación de nuevas oficinas.", "Instalación de aire acondicionado."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es uno de los propósitos de las barreras perimétricas?",
        "opciones": ["Embellecer el área.", "Crear un medio disuasivo físico o psicológico a la intrusión de personas ajenas a la institución.", "Delimitar áreas de jardín.", "Facilitar el paso de vehículos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué facilita una barrera perimétrica en relación con la observación y reacción del personal naval?",
        "opciones": ["La distracción del personal.", "Que cualquier elemento naval o los vigilantes observen, reaccionen y detengan al infractor.", "La relajación del personal.", "La disminución de la atención."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿A través de qué canaliza la circulación de personas y vehículos una barrera perimétrica?",
        "opciones": ["A través de cualquier punto de la barda.", "A través de accesos autorizados.", "A través de áreas verdes.", "A través de la periferia no protegida."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuándo se realiza la identificación y evaluación de los puntos y áreas vulnerables?",
        "opciones": ["Durante la fase de construcción.", "Durante el proceso de análisis de riesgos.", "Al finalizar el año fiscal.", "Cada vez que se cambia de personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuáles son algunos de los puntos vulnerables mencionados regularmente?",
        "opciones": ["Las canchas deportivas.", "Puertas y/o portones perimetrales en mal estado y/o sin vigilancia, ventanas, escaleras y azoteas colindantes a la calle o edificios contiguos, alcantarillas de ductos de aguas negras o grises, tanques de gas estacionario, almacén de combustible, plantas motogeneradoras de energía eléctrica, transformadores de energía eléctrica.", "Las áreas de comedor.", "Los pasillos principales."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué tipo de instalaciones son normalmente consideradas áreas vulnerables?",
        "opciones": ["Bibliotecas.", "Comandancias o Direcciones, Salas de Mando y Control, Oficialías de enlace, Centros de comunicaciones y cómputo, Polvorines, Pañol de Armamento y municiones, Cuerpos de agua colindantes, Hangares de Aviación, Patio de maniobras de vuelo, Helipuertos, Quirófanos, Accesos de personal y vehículos.", "Gimnasios.", "Estacionamientos para el personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cómo se clasifican las áreas restringidas con base en el análisis de riesgo y las políticas generales de seguridad de la información?",
        "opciones": ["Verdes, Amarillas y Rojas.", "Blancas, Grises y Negras.", "Altas, Medias y Bajas.", "Primarias, Secundarias y Terciarias."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué características tiene un 'Área Blanca'?",
        "opciones": ["Áreas con acceso libre.", "Áreas con máxima seguridad y control; son lugares de acceso restringido y controlados a través de sistemas electrónicos y/o revisiones permanentes del personal, artículos y accesorios personales.", "Áreas con control mínimo.", "Áreas de tránsito sin restricciones."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué tipo de control se aplica en un 'Área Gris'?",
        "opciones": ["Sin control alguno.", "Acceso restringido y control moderado, con ciertas medidas de seguridad en áreas comunes donde se presta servicio al público en general.", "Control extremo.", "Control aleatorio sin reglas fijas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué característica tiene un 'Área Negra'?",
        "opciones": ["Es el área más segura.", "Áreas con el mínimo de control en la cual se permite el tránsito del personal, como son las áreas periféricas de los establecimientos, es el área más vulnerable.", "Acceso únicamente para el Alto Mando.", "Requiere autorización especial para entrar."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué instrucción tendrá el personal de guardia de oficial de cuartel, día y guardia en prevención respecto a la presencia de desconocidos?",
        "opciones": ["Ignorar su presencia.", "Cuestionar la presencia de desconocidos no escoltados por personal autorizado y a cualquier persona que no exhiba una identificación visible.", "Darles la bienvenida.", "Pedirles que se retiren sin explicación."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué tipo de documentación y requisitos se deben cumplimentar para la acreditación del personal que podrá accesar y laborar en las Áreas Blancas?",
        "opciones": ["Solo el currículum vitae.", "Acuerdo de no revelación de información, Ficha de datos personales, Estudio de seguridad de personas, Evaluación del conocimiento del manejo de la información, Certificación de necesidad de acceso a la información, Estudio socio-económico, Evaluación psicológica, Examen toxicológico.", "Copia del pasaporte.", "Certificado de nacimiento."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cómo se les denominará a los activos prioritarios a proteger una vez identificados conforme al estudio de vulnerabilidad?",
        "opciones": ["Área Gris.", "Área Blanca.", "Área Negra.", "Área de Almacenamiento."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué mecanismos extras de refuerzo a la seguridad se podrán aplicar a un Área Blanca?",
        "opciones": ["Redes sociales.", "Enrejados metálicos, dispositivos electrónicos que prevean la proximidad y/o intrusión furtiva, cerraduras especiales, e incluso establecer un vigilante o grupo de vigilantes.", "Barreras de papel.", "Cámaras decorativas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es el propósito de la identificación y control de acceso?",
        "opciones": ["Determinar el número de visitantes diarios.", "Cerciorarse que se le permite la entrada a unidades y establecimientos navales, únicamente al personal y vehículos autorizados.", "Registrar la temperatura ambiente.", "Contar la cantidad de objetos que entran y salen."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se busca evitar con el control de accesos, además de permitir la entrada al personal autorizado?",
        "opciones": ["La llegada de correo.", "La introducción de dispositivos o componentes perjudiciales, la fuga de información y la malversación o robo de material o equipo de la instalación naval.", "La salida de basura.", "La entrada de luz solar."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué características debe tener el diseño de un gafete o tarjetón de identificación?",
        "opciones": ["Que sea fácil de copiar.", "Que represente máxima dificultad a cualquier intento para alterarlo o reproducirlo, debiendo ser rubricado por el Comandante o Director.", "Que tenga un diseño llamativo.", "Que sea de cualquier material disponible."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué información debe contener un gafete de identificación?",
        "opciones": ["Solo el nombre de la institución.", "Una fotografía reciente y nítida del portador, nombre del portador, nivel de acceso a las áreas restringidas, un número de control, fecha de expedición y vigencia, así como el nombre de la Institución, unidad o establecimiento al que pertenezca y área en que labora, agregando el cargo si lo tuviera.", "La fecha de nacimiento del portador.", "El número de teléfono personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cómo se dividirán los gafetes y tarjetones para civiles?",
        "opciones": ["Por tamaño.", "En gafetes y tarjetones para derechohabientes, visitantes y proveedores, asignándoles colores diferentes para su pronta identificación.", "Por tipo de letra.", "Por el año de expedición."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué significa que a un individuo se le otorga una autorización provisional para trabajar en un área restringida?",
        "opciones": ["Que no hay riesgo de seguridad.", "Que un individuo es un riesgo aceptable de seguridad hasta donde se pueda determinar.", "Que no se le permite el acceso.", "Que puede entrar sin supervisión."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "En ausencia de medios electrónicos o biométricos, ¿cuál es el método más seguro de establecer identificación positiva del personal?",
        "opciones": ["La pregunta de una contraseña.", "Invariablemente el reconocimiento visual de su identidad.", "La verificación del vehículo.", "La revisión de su vestimenta."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se exigirá al personal naval foráneo y/o desconocido visualmente para su identificación?",
        "opciones": ["Solo el uniforme.", "La identificación por medio de la credencial de alta seguridad y documentación que dio origen a su presencia en esa instalación.", "Una simple declaración verbal.", "Una fotografía de su rostro."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es el eslabón más vulnerable en cualquier reconocimiento del personal?",
        "opciones": ["La tecnología de identificación.", "La desidia o apatía por parte del personal de guardia para comparar al portador con la credencial de identidad mostrada.", "La calidad de las credenciales.", "El número de personas que entran."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cómo se puede lograr mayor seguridad en el acceso a unidades y establecimientos navales mediante el uso de listas?",
        "opciones": ["Con una lista aleatoria de nombres.", "Mediante el uso de una lista impresa con nombres del personal naval o proveedores autorizados para ingresar.", "Con una lista de compras.", "Con una lista de contactos personales."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué debe ocurrir si una persona no aparece en la lista de acceso?",
        "opciones": ["Se le permitirá la entrada sin preguntas.", "Se le negará la entrada a cualquier persona que no justifique plenamente la legitimidad del ingreso, informando al jefe de seguridad.", "Se le pedirá que espere indefinidamente.", "Se le ofrecerá una identificación provisional sin verificación."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cómo deben ser los gafetes personales o tarjetones vehiculares para visitantes?",
        "opciones": ["De cualquier tamaño y color.", "De fácil identificación tanto por tamaño como por color, para permitir que personal naval mantenga contacto visual con mayor atención durante su estancia al interior de las instalaciones navales.", "Completamente discretos.", "Solo con el nombre del visitante."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Quién debe acompañar permanentemente a los visitantes?",
        "opciones": ["Nadíe.", "Personal naval de guardia.", "Otro visitante.", "Un guía turístico."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "En el caso de visitantes distinguidos, ¿quién designará al acompañante?",
        "opciones": ["El propio visitante.", "El comandante o director.", "Un miembro del personal de cocina.", "Un conductor."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué deben entregar los contratistas para realizar una construcción o remodelación en una unidad o establecimiento naval?",
        "opciones": ["Un plano de la construcción.", "Una relación de empleados con nombre, apellidos, edad, sexo, puesto o cargo para permitir el acceso.", "Una lista de materiales.", "Un presupuesto detallado."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué debe hacer cualquier elemento naval si detecta contratistas en áreas restringidas o con actitudes sospechosas?",
        "opciones": ["Ignorarlos.", "Informar de inmediato al jefe de seguridad u oficiales de guardia.", "Preguntarles qué están haciendo.", "Ofrecerles ayuda."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué deben verificar antes de admitir al personal de mantenimiento de servicios públicos o comerciales en una instalación naval?",
        "opciones": ["Que lleven insignias de su compañía.", "Que el servicio que presta haya sido solicitado por los conductos regulares y autorizado por el comandante o director de la unidad o establecimiento naval.", "Su estado de salud.", "Su número de teléfono."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se debe hacer ante la mínima duda sobre el personal de mantenimiento?",
        "opciones": ["Permitirles el paso.", "Consultar con el jefe de seguridad en forma personal y directa.", "Posponer la entrada.", "Pedir una segunda opinión al portero."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué regla se aplica a la entrada y salida de paquetes en las unidades y establecimientos navales?",
        "opciones": ["Se permite sin inspección.", "No se debe permitir la entrada ni salida de paquetes sin previa inspección y autorización.", "Se permite solo si son de tamaño pequeño.", "Se permite solo si el contenido es conocido."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se debe verificar al inspeccionar los paquetes que se reciben?",
        "opciones": ["El color del paquete.", "Que son entregados por servicios de paquetería y mensajería conocidos que utilicen preferentemente uniformes y vehículos oficiales exigiendo identificación oficial y de la empresa.", "La marca del paquete.", "Si el paquete está envuelto para regalo."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Dónde deben estar alejadas las áreas de estacionamiento para vehículos de propiedad privada, siempre que sea factible?",
        "opciones": ["Cerca de la entrada principal.", "De un área en la que pudiera causar daños o pérdidas de vidas por explosión.", "Junto a las áreas de descanso.", "En el interior de los edificios."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es el método de estacionamiento preferente?",
        "opciones": ["En fila india.", "En batería.", "En diagonal.", "En doble fila."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es el propósito de la colocación de letreros y señalizaciones de seguridad?",
        "opciones": ["Decorar las paredes.", "Comunicar a todo el personal propio y ajeno las prohibiciones o indicaciones que se consideren necesarias para coadyuvar en los controles y medidas de seguridad al interior de las unidades y establecimientos navales.", "Promocionar eventos futuros.", "Indicar la dirección de la salida de emergencia solamente."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se debe tener en cuenta al colocar letreros y señalizaciones de seguridad?",
        "opciones": ["Que sean pequeños y discretos.", "Que las dimensiones y colocación de los mismos, permitan ser leídos y comprendidos con facilidad.", "Que sean de un solo color.", "Que contengan imágenes complejas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es el propósito del alumbrado en las instalaciones?",
        "opciones": ["Crear un ambiente acogedor.", "Obtener un nivel de iluminación óptimo en una función específica.", "Proporcionar calor en invierno.", "Consumir la mayor cantidad de energía posible."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué debe hacer el alumbrado en las horas de oscuridad?",
        "opciones": ["Proyectar sombras largas.", "Alumbrar intensiva y continuamente un área determinada con conos de luz que se traslapen.", "Iluminar solo los puntos específicos.", "Parpadear para llamar la atención."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuáles son los métodos principales de iluminación continua?",
        "opciones": ["Iluminación directa y reflectante.", "Proyección de resplandor e iluminación controlada.", "Iluminación natural y artificial.", "Iluminación de baja y alta intensidad."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Para qué es útil la 'Proyección de resplandor'?",
        "opciones": ["Para crear un efecto artístico.", "Donde el resplandor de las luces, dirigido a través del territorio circundante no estorba las operaciones adyacentes, permitiendo al vigilante ver el área exterior mientras lo protege de la vista de un posible intruso.", "Para señalizar áreas de recreación.", "Para indicar la presencia de vehículos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué caracteriza la 'Iluminación controlada'?",
        "opciones": ["No tiene control sobre el ancho de la franja iluminada.", "El ancho de la franja iluminada puede ser controlado y ajustado para que se adapte a la necesidad en particular.", "Solo se utiliza en interiores.", "Es un tipo de iluminación intermitente."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },

    # Bloque 3 de 6: Preguntas 101-150
    {
        "pregunta": "¿Qué se debe considerar en el alumbrado como sistema de emergencia?",
        "opciones": ["Un sistema que pueda suplir los sistemas de iluminación continua.", "Luces decorativas para festividades.", "Un sistema que solo funcione durante el día.", "Iluminación para áreas de estacionamiento exclusivamente."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Hacia dónde deben estar dirigidos los conos de iluminación de las unidades del alumbrado?",
        "opciones": ["Hacia arriba, iluminando el cielo.", "Hacia abajo y en dirección contraria de las unidades y establecimientos navales o de un área protegida, así como del personal de vigilantes.", "Directamente hacia las instalaciones para evitar sombras.", "Hacia el exterior sin ninguna dirección específica."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cómo deben estar dispuestas las unidades de alumbrado para el personal de vigilantes?",
        "opciones": ["Para crear el máximo resplandor.", "De tal manera que se forme un mínimo de sombras y un mínimo de resplandor en los ojos de los vigilantes.", "Sin considerar la visión de los vigilantes.", "En una sola línea sin traslape."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Dónde deben estar ubicadas las unidades de alumbrado para la barrera perimetral?",
        "opciones": ["Lejos de la barrera perimetral.", "A suficiente distancia dentro del área protegida y por encima de la barrera, de modo que la luz que emite sobre el terreno incluya un área tanto en la parte de adentro como en la de afuera.", "Exclusivamente en la parte de afuera de la barrera.", "Dentro de los edificios para evitar ser dañadas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué función cumplen los sistemas de vigilancia de circuito cerrado?",
        "opciones": ["Reemplazan completamente a los vigilantes.", "Son medios auxiliares a la función de los vigilantes, sin embargo no los sustituyen.", "Solo sirven para grabar eventos pasados.", "Son únicamente para el registro de entrada de vehículos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Por qué debe ser respaldada la vigilancia con circuito cerrado?",
        "opciones": ["Por un equipo de limpieza.", "Por una Fuerza de Reacción que actúe en caso de detectarse situaciones de amenaza.", "Por un sistema de megafonía.", "Por un grupo de historiadores."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Dónde se considera la colocación de sistemas de vigilancia de circuito cerrado?",
        "opciones": ["En áreas de descanso.", "En áreas críticas o restringidas.", "En todas las áreas sin distinción.", "Solo en las oficinas administrativas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué capacidad debe tener el personal de monitoreo de circuito cerrado?",
        "opciones": ["Entender varios idiomas.", "Estar capacitado para interpretar el lenguaje corporal que denote amenazas.", "Manejar software de edición de video.", "Memorizar números telefónicos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué es el servicio de la Guardia en Prevención?",
        "opciones": ["Una actividad recreativa para el personal naval.", "Servicio efectuado por un personal naval de los diferentes cuerpos y servicios capacitados y adiestrados para la vigilancia y/o defensa de las unidades y establecimientos navales, con el objeto de dar seguridad y conservar el orden conforme a las leyes y reglamentos vigentes en la materia.", "Una tarea administrativa.", "Un ejercicio de simulacro sin consecuencias reales."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿De qué varía la constitución de la guardia en prevención?",
        "opciones": ["Del clima del día.", "De acuerdo al tamaño y disposición de las unidades y establecimientos navales.", "Del número de visitantes.", "Del tipo de eventos programados."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es el propósito del establecimiento de la guardia en prevención?",
        "opciones": ["Control efectivo de la fuerza de guardia y garantizar una seguridad adecuada a las actividades y funciones principales.", "Reducir el número de personal necesario.", "Aumentar el tiempo de respuesta.", "Simplificar los procedimientos de seguridad."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Dónde se ubicará la comandancia de la guardia en una instalación naval para ejercer un mejor control, crear disuasión y reaccionar de manera inmediata?",
        "opciones": ["En el centro de la instalación.", "En la entrada principal o cerca de ésta.", "En la parte trasera del establecimiento.", "En cualquier lugar conveniente."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cómo se establecerán los puestos de vigilancia?",
        "opciones": ["De manera aleatoria.", "De tal manera que cubran la periferia, manteniendo una proximidad visual entre ellos con el objeto de reaccionar con prontitud ante alguna amenaza.", "Solo en los puntos de entrada.", "En el interior de los edificios sin visibilidad externa."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se considerará establecer en los puntos y áreas vulnerables como resultado del análisis y evaluación de los riesgos?",
        "opciones": ["Jardines.", "Vigilantes.", "Fuentes de agua.", "Áreas de descanso."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué tipo de consignas se deben expedir a los elementos integrantes de la guardia en prevención?",
        "opciones": ["Consignas verbales y flexibles.", "Consignas generales y especiales por escrito que incluyan el mayor número de ordenamientos para garantizar la ejecución del servicio de guardia de forma eficiente y efectiva.", "Consignas ambiguas para interpretación personal.", "Consignas que cambian diariamente."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Con qué frecuencia deben revisarse y actualizarse las consignas?",
        "opciones": ["Cada año.", "Periódicamente en lapsos de seis meses.", "Solo cuando hay un incidente.", "Nunca, una vez establecidas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "Además de las consignas, ¿qué es importante que los servicios de guardia resguarden, conozcan y apliquen?",
        "opciones": ["Noticias del día.", "Las directivas e instrucciones emitidas por el Alto Mando o Mandos Superiores.", "Historias de guerra.", "Recetas de cocina."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿A quién puede solicitar apoyo el oficial de guardia en prevención si la unidad tiene una Fuerza de Reacción Inmediata y existe peligro inminente que supere la capacidad propia?",
        "opciones": ["Al personal administrativo.", "Al capitán de permanencia el apoyo de ésta Fuerza.", "A las unidades vecinas sin autorización.", "Al personal de cocina."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué son los sistemas de comunicaciones en el contexto de seguridad?",
        "opciones": ["Solo teléfonos móviles.", "Un conjunto de medios, material, instalaciones, personal idóneo, doctrina y organización adecuada requeridos para establecer y mantener enlaces de comunicaciones confiables, seguros y rápidos.", "Sistemas de entretenimiento.", "Equipos de navegación."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué debe existir para cada unidad o establecimiento naval en relación con las comunicaciones?",
        "opciones": ["Un plan de comunicaciones turístico.", "Un plan táctico simplificado de comunicaciones.", "Un plan de comunicaciones social.", "Un plan de comunicaciones para desfiles."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué función tienen las señales audibles y visibles como medios de apoyo a los sistemas de comunicación?",
        "opciones": ["Retrasar la comunicación.", "Previo acuerdo en el uso de las mismas, activar un plan de zafarrancho facilitando la comunicación instantánea del mismo.", "Crear confusión.", "Sustituir completamente las comunicaciones verbales."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "Además de las medidas de protección física, ¿qué debe tener cada instalación naval para reducir al mínimo los efectos de un desastre de gran proporción?",
        "opciones": ["Planes de vacaciones.", "Planes de contingencia actualizados.", "Planes de construcción.", "Planes de reforestación."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué deben considerar los planes de contingencia?",
        "opciones": ["Solo los recursos materiales.", "Todo el efectivo de la unidad o establecimiento naval en una acción conjunta para combatir la amenaza común.", "Únicamente la respuesta del personal de guardia.", "Los eventos deportivos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué puede garantizar un plan cuidadosamente organizado y practicado?",
        "opciones": ["Una reacción lenta y confusa.", "Una reacción rápida y eficaz a cualquier situación que pueda ocurrir.", "Un aumento de los riesgos.", "La inacción del personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué producirá el análisis y discusión serena en la etapa de planeamiento de los planes de contingencia?",
        "opciones": ["Descoordinación.", "Mejoras en la coordinación, ejecución y resultados, en el menor tiempo posible.", "Retrasos en la ejecución.", "Complicaciones innecesarias."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Con qué frecuencia deberán ponerse en práctica los planes de contingencia y con qué propósito?",
        "opciones": ["Una vez al año, para cumplir con el requisito.", "Una vez a la semana, para detectar inconsistencias, aplicar mejoras a los planes y familiarizar al personal naval en la ejecución.", "Solo en situaciones de emergencia real.", "Cuando el personal tenga tiempo libre."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuáles son los planes de contingencia básicos que deberá elaborar una unidad o establecimiento naval?",
        "opciones": ["Plan de construcción, Plan de limpieza, Plan de vacaciones.", "Plan de Defensa, Plan de Contraincendio, Plan de Evacuación.", "Plan de socialización, Plan de entretenimiento, Plan de transporte.", "Plan de inventario, Plan de mantenimiento, Plan de reclutamiento."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué horarios se deben considerar para la ejecución de los planes de contingencia?",
        "opciones": ["Solo horario de oficina.", "Horario laborable (todo el personal presente) y en horario no laborable (solo personal de guardia).", "Solo horario nocturno.", "Solo horario de fin de semana."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué comprende la cultura de seguridad, según el concepto?",
        "opciones": ["Solo los reglamentos escritos.", "Las actitudes y valores del personal de la Secretaría de Marina Armada de México de manera institucional en los aspectos relativos a la seguridad física, tanto en la forma de entenderla como la aplicación en el comportamiento rutinario.", "Las preferencias personales del personal.", "El equipo de seguridad utilizado."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Cómo se percibe la cultura de seguridad física?",
        "opciones": ["Como la conducta individual de cada persona.", "Como la conducta observada en cada uno de los miembros de la Secretaría de Marina Armada de México como un todo institucional, sin considerar la individualidad de las personas.", "Como un conjunto de reglas sin aplicación práctica.", "Como una teoría abstracta."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué significa si la cultura de seguridad física se observa fuerte?",
        "opciones": ["Que el personal está relajado.", "Esto literalmente se traduce en una fortaleza de seguridad institucional.", "Que no se necesita más entrenamiento.", "Que los riesgos han desaparecido."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué sucede con los eventos aislados por falta de cultura de seguridad física?",
        "opciones": ["No tienen impacto.", "Se suman para deteriorar o disminuir esa fortaleza de seguridad institucional.", "Fortalecen la seguridad.", "Pasan desapercibidos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Cómo se ha construido la imagen pública y el prestigio institucional de la Secretaría de Marina - Armada de México?",
        "opciones": ["Con campañas de publicidad.", "A lo largo de muchos años de dedicación, esfuerzos y sacrificios de los integrantes de esta noble institución.", "A través de la casualidad.", "Con inversiones financieras."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué requiere la imagen pública y el prestigio institucional que posee la SEMAR hoy?",
        "opciones": ["Una disminución de la seguridad.", "La adopción de una cultura de seguridad física que impulse la sinergia necesaria para responder a las amenazas actuales, reduciendo las vulnerabilidades y minimizando los riesgos.", "Un cambio en la misión institucional.", "Una reorganización completa de personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Cuál es la meta de un programa de educación en relación a la cultura de seguridad física?",
        "opciones": ["Solo informar al personal de guardia.", "Familiarizar y concientizar a todo el personal naval sobre la importancia de la adopción de medidas de seguridad.", "Reducir el conocimiento del personal.", "Promover la desorganización."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué pretende transformar el programa de educación en cultura de seguridad física?",
        "opciones": ["La individualidad de las personas.", "La idiosincrasia de la responsabilidad individual del personal naval que se encuentra de guardia a un pensamiento doctrinario en donde todos los integrantes somos responsables de la seguridad física de las instalaciones navales, aún sin estar nombrado en el servicio de guardia.", "Las prioridades del Alto Mando.", "Los objetivos de la institución."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Cómo se adquiere el estar consciente de la importancia de la seguridad física?",
        "opciones": ["Es un estado inherente de la mente.", "A través del conocimiento y la experiencia del personal naval.", "Por intuición.", "Por nacimiento."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué valor tienen las estructuras y procedimientos implementados para minimizar los riesgos sin el apoyo activo de todo el personal naval?",
        "opciones": ["Tienen un valor agregado considerable.", "No tienen ningún valor agregado.", "Son parcialmente útiles.", "Son suficientes por sí mismos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué debe estar consciente el personal naval en relación con las amenazas?",
        "opciones": ["Que las amenazas son estáticas.", "De la dinámica de las amenazas de los grupos antagónicos a las instituciones del Estado.", "Que las amenazas son irrelevantes.", "Que las amenazas solo afectan a otros."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿De quién es la responsabilidad individual para descubrir y frustrar planes o acciones en contra de la seguridad física?",
        "opciones": ["Solo del jefe de seguridad.", "Una responsabilidad compartida por todos los miembros que integran la Secretaría de Marina - Armada de México.", "Solo del personal de inteligencia.", "Solo del personal de guardia."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué se hace necesario para la responsabilidad compartida en seguridad física?",
        "opciones": ["Un programa opcional de entrenamiento.", "Un programa continuo y obligatorio de educación que garantice el desarrollo de la cultura de seguridad física.", "Un programa de reducción de personal.", "Un programa de ocio."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué se genera con el programa continuo y obligatorio de educación en seguridad física?",
        "opciones": ["La fragmentación de la conciencia.", "La unificación de la conciencia que la seguridad física exitosa demanda.", "La confusión entre el personal.", "La disminución de la moral."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué incluyen los requerimientos mínimos de un programa eficaz de seguridad física de las unidades y establecimientos navales?",
        "opciones": ["Solo el equipo de seguridad.", "Voluntad y apoyo directo del Comandante o Director de la instalación naval, implementación del programa a cargo del jefe de seguridad, selección de un cuadro de instructores, impartición de academias y conferencias obligatorias, y evaluación del programa.", "Solo la evaluación del personal.", "Únicamente la adquisición de nuevas tecnologías."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿De quién está a cargo la implementación del programa de seguridad física?",
        "opciones": ["Del personal de limpieza.", "Del jefe de seguridad.", "Del personal médico.", "De los proveedores externos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿A quiénes se debe impartir academias y conferencias obligatorias como parte del programa?",
        "opciones": ["Solo al personal administrativo.", "A todo el personal naval involucrado en los servicios de guardia, tanto de armas como de apoyo.", "Únicamente al Alto Mando.", "A nadie, ya que es información confidencial."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Para qué se realiza la evaluación del programa, los instructores y el personal naval participante?",
        "opciones": ["Para asignar sanciones.", "Para una retroalimentación que permita mejorar los programas de forma permanente y continua.", "Para registrar la asistencia solamente.", "Para determinar quién es el mejor estudiante."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué se mantiene vigente para la apropiación del aprendizaje en la 'Sublimidad del Mensaje'?",
        "opciones": ["La lectura de libros de texto.", "La observación repetida de mensajes colocados en cartelones, lonas y folletos.", "La transmisión oral de información.", "Las reuniones formales."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué se permite con el uso de recursos gráficos como cartelones, lonas y folletos?",
        "opciones": ["La confusión del mensaje.", "Una fácil comprensión de la importancia de la seguridad en las unidades y establecimientos navales.", "La complicación de la información.", "La distracción del personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Dónde es necesario colocar los cartelones y lonas para su aplicación en la concientización general?",
        "opciones": ["En lugares ocultos.", "En lugares visibles y de acceso general para todo el personal.", "Solo en las oficinas de los jefes.", "Fuera de las instalaciones."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },

    # Bloque 4 de 6: Preguntas 151-200
    {
        "pregunta": "Según el ANEXO 'A', ¿cuál es una de las funciones y responsabilidades del Capitán u Oficial nombrado como Jefe de Seguridad Física?",
        "opciones": ["Gestionar los eventos sociales.", "Asesorar al mando y mantenerlo informado en todo lo relacionado con la seguridad física de las Instalaciones navales.", "Realizar el inventario de la comida.", "Decorar las oficinas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué debe adecuar e implantar el Jefe de Seguridad Física para preservar la integridad del personal naval, el material y las instalaciones?",
        "opciones": ["Nuevas políticas de vestimenta.", "Los mecanismos de protección.", "Horarios de descanso.", "Planes de celebración."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué debe identificar el Jefe de Seguridad en su área de responsabilidad y qué metodologías aplicar, en coordinación con el Oficial de Seguridad de la Información (OSI)?",
        "opciones": ["Los procesos de alimentación y métodos de cocina.", "Los procesos críticos y aplicar las metodologías establecidas por la CSI para realizar análisis de riesgo y administrar las vulnerabilidades y fortalezas de los sistemas de información.", "Los procesos de transporte y métodos de viaje.", "Los procesos de entretenimiento y métodos de diversión."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué áreas de seguridad debe definir el Jefe de Seguridad, en coordinación con el Oficial de Seguridad de la Información (OSI) y en base al análisis de riesgo?",
        "opciones": ["Área Verde, Área Amarilla, Área Roja.", "Área Blanca, Área Gris, Área Negra.", "Área de Producción, Área de Almacenamiento, Área de Distribución.", "Área de Trabajo, Área de Descanso, Área de Tránsito."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué característica tiene el 'Área Blanca' según las funciones del Jefe de Seguridad?",
        "opciones": ["Área con mínimo control.", "Área con máxima seguridad.", "Área de acceso libre.", "Área de tránsito."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué característica tiene el 'Área Gris' según las funciones del Jefe de Seguridad?",
        "opciones": ["Área de acceso restringido.", "Área de seguridad máxima.", "Área con libre acceso.", "Área de desorden."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué característica tiene el 'Área Negra' según las funciones del Jefe de Seguridad?",
        "opciones": ["Área con control total.", "Área con el mínimo de control.", "Área sin riesgo.", "Área de acceso para personal autorizado."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué debe mantener actualizada el Jefe de Seguridad?",
        "opciones": ["La lista de vacaciones.", "La agenda de riesgo de la Unidad.", "El menú del comedor.", "Los horarios de ejercicios."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿En base a qué parámetros debe definir el Jefe de Seguridad las áreas vulnerables?",
        "opciones": ["La antigüedad del edificio y el número de ventanas.", "Facilidad de ingreso a las instalaciones por carecer de cercos o por encontrase estos en mal estado, y su colindancia con edificios civiles, escuelas o centros de trabajos que merezcan atención especial.", "El tipo de material de construcción y el color de las paredes.", "La cantidad de personal y la calidad del mobiliario."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué debe ejecutar y promover el Jefe de Seguridad en todo el personal de su unidad?",
        "opciones": ["El plan de entretenimiento.", "El plan de concientización y promover la doctrina en materia de seguridad física.", "El plan de mejoras salariales.", "El plan de vacaciones."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué debe implementar el Jefe de Seguridad por medio de zafarranchos a diversas horas para garantizar el pleno conocimiento por todo el personal naval?",
        "opciones": ["El plan de limpieza.", "La aplicación continua del Plan de Contingencias.", "El plan de construcción.", "El plan de eventos sociales."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué debe aplicar y vigilar el Jefe de Seguridad para asegurar el buen funcionamiento de todos los procesos, directivas y recomendaciones en materia de seguridad?",
        "opciones": ["Las normas de vestimenta.", "El cumplimiento de la legislación vigente y de la normatividad emitida por el Estado Mayor General de la Armada.", "Los protocolos de comunicación informal.", "Las instrucciones de decoración."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué debe supervisar y evaluar continuamente el Jefe de Seguridad?",
        "opciones": ["La asistencia a reuniones.", "Las áreas vulnerables y los mecanismos implementados para mejorar la seguridad de las instalaciones navales.", "El consumo de energía eléctrica.", "El inventario de suministros de oficina."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Cómo debe atender y responder el Jefe de Seguridad a las notificaciones de sospecha de un posible incidente de violación a la seguridad física o incidente real?",
        "opciones": ["Sin prioridad alguna.", "De inmediato.", "Al final del día laboral.", "Cuando tenga tiempo disponible."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué debe informar el Jefe de Seguridad al Mando sobre los accesos no autorizados o incumplimiento de directivas?",
        "opciones": ["Detalles sin importancia.", "Para que se apliquen las sanciones correspondientes de acuerdo con la naturaleza de la intrusión o los daños ocasionados.", "Solicitudes de nuevos equipos.", "Información sobre eventos pasados."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "Según el ANEXO 'B', ¿qué es lo primero en la 'Lista de Verificación para la Seguridad Física de las Instalaciones Navales'?",
        "opciones": ["Registro de visitantes.", "Nombramiento del Jefe de Seguridad Física.", "Plan de Cultura de Seguridad.", "Consignas de los servicios de guardia."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué tipo de análisis se incluye en la lista de verificación del ANEXO 'B'?",
        "opciones": ["Análisis financiero.", "Análisis de Riesgo de la Unidad y Establecimiento Naval.", "Análisis de personal.", "Análisis de mercado."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué tipo de agenda se incluye en la lista de verificación del ANEXO 'B'?",
        "opciones": ["Agenda de reuniones.", "Agenda de Riesgo de la Unidad y Establecimiento Naval.", "Agenda de eventos.", "Agenda de contactos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué estudio se menciona en la lista de verificación para el establecimiento del servicio de Guardia en Prevención?",
        "opciones": ["Estudio de mercado.", "Estudio de Estado Mayor.", "Estudio de viabilidad.", "Estudio de impacto ambiental."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué tipo de planes se incluyen en la lista de verificación del ANEXO 'B'?",
        "opciones": ["Plan de Contingencias y Plan de Cultura de Seguridad.", "Plan de Construcción y Plan de Mantenimiento.", "Plan de Contratación y Plan de Despido.", "Plan de Marketing y Plan de Ventas."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué tipo de programa se incluye en la lista de verificación para el desempeño del Servicio de Guardia en Prevención?",
        "opciones": ["Programa de ocio.", "Programa de capacitación.", "Programa de festividades.", "Programa de transporte."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué tipo de registro se menciona en la lista de verificación respecto a la evaluación del personal?",
        "opciones": ["Registro de asistencia.", "Registro de la evaluación practicada al personal que desempeña el servicio de guardia.", "Registro de salarios.", "Registro de vacaciones."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué expediente se incluye en la lista de verificación relacionado con los informes recibidos por el Jefe de Seguridad?",
        "opciones": ["Expediente de informes de vacaciones.", "Expediente de informes recibidos referente a la Seguridad Física.", "Expediente de informes de gastos.", "Expediente de informes de eventos sociales."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué expediente se incluye en la lista de verificación relacionado con las acciones y respuestas del Jefe de Seguridad Física?",
        "opciones": ["Expediente de quejas.", "Expediente de acciones y respuestas dadas por el Jefe de Seguridad Física.", "Expediente de promociones.", "Expediente de sugerencias."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué programa se incluye en la lista de verificación relacionado con las prácticas de zafarranchos?",
        "opciones": ["Programa de visitas.", "Programa de prácticas de zafarranchos derivados del Plan de Contingencias.", "Programa de mantenimiento de vehículos.", "Programa de registro de documentos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué se debe registrar sobre las prácticas de zafarranchos para la mejora continua?",
        "opciones": ["Solo la fecha.", "Registro de prácticas de los zafarranchos con memoria fotográfica, observaciones y recomendaciones para la mejora continua.", "Únicamente los participantes.", "El tipo de comida servida."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué tipo de registro se incluye en la lista de verificación para visitas y proveedores?",
        "opciones": ["Registro de llamadas.", "Registro de tarjetones, credenciales para visitas, proveedores, etc.", "Registro de entregas de paquetería.", "Registro de reuniones."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué busca garantizar el manual DAM 1.3.4.6?",
        "opciones": ["Solo la disciplina militar.", "La seguridad de los recursos humanos, materiales y financieros en las Unidades y Establecimientos navales de la Secretaría de Marina Armada de México.", "La eficiencia administrativa.", "El bienestar social."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "General"
    },
    {
        "pregunta": "¿Qué tipo de incidentes han trastocado las percepciones de seguridad en las instalaciones navales?",
        "opciones": ["Incremento en el turismo.", "Ataques directos por parte de la delincuencia organizada, robo y/o pérdida de material clasificado y fuga de información.", "Nuevas regulaciones de tráfico.", "Cambios en la moda militar."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Introducción"
    },
    {
        "pregunta": "¿Qué tipo de capacidades del personal se están actualizando según el documento?",
        "opciones": ["Capacidades de cocina.", "Capacidades de seguridad.", "Capacidades de canto.", "Capacidades de jardinería."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Introducción"
    },
    {
        "pregunta": "¿Quiénes asumen roles necesarios e importantes durante la implementación de los planes de seguridad y contingencia, además de la guardia en prevención?",
        "opciones": ["Únicamente el personal de limpieza.", "Ambas guardias (de armas y de apoyo).", "Solo el jefe de seguridad.", "El personal administrativo."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué pueden causar los riesgos en las unidades y establecimientos navales, además de la pérdida o daño de recursos?",
        "opciones": ["Un aumento de la eficiencia.", "Desorganización y la pérdida de la eficiencia y efectividad en el cumplimiento de la misión.", "Una mejora en el ambiente laboral.", "Mayor productividad."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué es un ejemplo de riesgo natural que también puede ser inducido por acción humana?",
        "opciones": ["Terremoto.", "Inundación e Incendio.", "Tsunami.", "Tormenta."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Cuál es la función del Oficial de Seguridad de la Información (OSI) en la organización de la seguridad física?",
        "opciones": ["Se encuentra bajo el mando del jefe de seguridad y es ejecutante de la acción planeada.", "Realizar labores administrativas.", "Gestionar el transporte.", "Preparar alimentos."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué permite un sistema y plan de comunicaciones eficiente y efectivo a todos los elementos de guardia?",
        "opciones": ["Mantenerse aislados.", "Mantener una intercomunicación.", "Realizar llamadas personales.", "Ignorar las alertas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué incluye el registro y control en relación con los vehículos de proveedores?",
        "opciones": ["Solo el color del vehículo.", "El registro de vehículos de proveedores.", "La marca del vehículo.", "El año del vehículo."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué debe llevar el personal naval para su identificación, según el documento?",
        "opciones": ["Un brazalete.", "Credencial de alta seguridad.", "Un gorro especial.", "Una flor en el bolsillo."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué tipo de acciones contra las unidades y establecimientos navales se incluyen en los riesgos antropogénicos?",
        "opciones": ["Solo los descuidos.", "Actos intencionales de comisión u omisión que incluyen todas las acciones ocultas o abiertas.", "Solamente accidentes.", "Eventos climáticos extremos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué se debe realizar con la planificación de seguridad física cuando existen cambios estructurales o tecnológicos?",
        "opciones": ["Ignorarla.", "Revisar y actualizar.", "Eliminarla.", "Archivarla sin cambios."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué función tienen las edificaciones de la Sala de Guardia y Puestos de Vigilancia?",
        "opciones": ["Almacenar equipos viejos.", "Alojar o establecer al personal de guardia para ser empleados de manera inmediata en caso de una situación contingente.", "Proporcionar un espacio para el descanso prolongado.", "Servir como punto de reunión social."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué medidas de seguridad se deben aplicar en un Área Blanca, además de las que le corresponden por su estatus?",
        "opciones": ["Medidas de relajación.", "Mecanismos extras de refuerzo a la seguridad tales como enrejados metálicos, dispositivos electrónicos, cerraduras especiales, o establecer vigilantes.", "Medidas de flexibilización.", "Medidas de acceso libre."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué tipo de identificación es necesaria para todo el personal que labora en las áreas restringidas?",
        "opciones": ["Una camiseta de color brillante.", "Uso de identificación.", "Una señal secreta.", "Un brazalete temporal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué ocurre si el personal naval foráneo o desconocido visualmente no porta el uniforme u ostenta jerarquía de superioridad al ser solicitado para identificación?",
        "opciones": ["Se le permite el acceso sin más preguntas.", "Se le exige la identificación por medio de la credencial de alta seguridad y documentación.", "Se le ofrece un puesto de trabajo.", "Se le da un recorrido por las instalaciones."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué debe verificar el personal de guardia con cada portador de credencial o tarjetón?",
        "opciones": ["Su color de cabello.", "Que sea verificado con la lista.", "Su altura.", "Su fecha de nacimiento."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es la función principal de los letreros y señalizaciones de seguridad?",
        "opciones": ["Embellecer las paredes.", "Comunicar prohibiciones o indicaciones para coadyuvar en los controles y medidas de seguridad.", "Servir de decoración.", "Indicar la ubicación de los baños."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué tipo de riesgos causarán desorganización y la pérdida de la eficiencia y efectividad en el cumplimiento de la misión?",
        "opciones": ["Riesgos de seguridad.", "Riesgos de comunicación.", "Riesgos financieros.", "Riesgos de planificación."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué son los riesgos de seguridad en las unidades y establecimientos navales?",
        "opciones": ["Condiciones que solo mejoran el desempeño.", "Condiciones que pueden dar como resultado la pérdida o daño de recursos humanos, materiales y financieros.", "Elementos decorativos.", "Procesos de mejora continua."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué tipo de riesgos se generan por descuidos humanos o actos intencionales?",
        "opciones": ["Riesgos naturales.", "Riesgos antropogénicos.", "Riesgos económicos.", "Riesgos operativos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué se debe hacer con la ubicación de la comandancia de la guardia?",
        "opciones": ["Que esté en la entrada principal o cerca de esta para ejercer mejor control, crear disuasión y reaccionar de inmediato.", "Que esté en un lugar escondido.", "Que esté lejos de la entrada principal.", "Que esté en un área de descanso."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué elemento de seguridad física ayuda a retrasar y obstaculizar el acceso de un intruso?",
        "opciones": ["La señalización.", "Las barreras perimétricas.", "La iluminación.", "Los sistemas de comunicación."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué tipo de información se considera clasificada en el contexto de seguridad física?",
        "opciones": ["Información personal del personal.", "Material susceptible de robo y/o pérdida.", "Documentos de entretenimiento.", "Noticias generales."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },

    # Bloque 5 de 6: Preguntas 201-250
    {
        "pregunta": "¿Qué tipo de riesgos causarán desorganización y la pérdida de la eficiencia y efectividad en el cumplimiento de la misión?",
        "opciones": ["Riesgos de seguridad.", "Riesgos de comunicación.", "Riesgos financieros.", "Riesgos operativos."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué son los riesgos en las unidades y establecimientos navales, según el documento?",
        "opciones": ["Condiciones que solo mejoran el desempeño.", "Condiciones que pueden dar como resultado la pérdida o daño de recursos humanos, materiales y financieros.", "Elementos decorativos.", "Procesos de mejora continua."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué tipo de riesgos se generan por descuidos humanos o actos intencionales?",
        "opciones": ["Riesgos naturales.", "Riesgos antropogénicos.", "Riesgos económicos.", "Riesgos operativos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué se debe hacer con la ubicación de la comandancia de la guardia?",
        "opciones": ["Que esté en la entrada principal o cerca de esta para ejercer mejor control, crear disuasión y reaccionar de inmediato.", "Que esté en un lugar escondido.", "Que esté lejos de la entrada principal.", "Que esté en un área de descanso."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué elemento de seguridad física ayuda a retrasar y obstaculizar el acceso de un intruso?",
        "opciones": ["La señalización.", "Las barreras perimétricas.", "La iluminación.", "Los sistemas de comunicación."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué tipo de información se considera clasificada en el contexto de seguridad física, según las vulnerabilidades comunes?",
        "opciones": ["Información personal del personal.", "Material susceptible de robo y/o pérdida.", "Documentos de entretenimiento.", "Noticias generales."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Qué se requiere para la identificación positiva del personal en ausencia de medios electrónicos o biométricos?",
        "opciones": ["Solo la firma.", "El reconocimiento visual de su identidad.", "La huella dactilar.", "El código de barras."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es el objetivo principal del manual DAM 1.3.4.6?",
        "opciones": ["Promover actividades recreativas.", "Orientar y normar la actuación del personal de la Secretaría de Marina Armada de México para el mantenimiento de la seguridad de las Unidades y Establecimientos navales.", "Establecer planes de vacaciones.", "Registrar el clima diario."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "¿Qué importancia tiene el conocimiento del modelo doctrinario para el personal naval?",
        "opciones": ["Es irrelevante para sus funciones diarias.", "Norma las características, procedimientos, equipo y material empleado para la seguridad de las instalaciones navales.", "Solo aplica a personal administrativo.", "Es un documento de referencia ocasional."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "¿Quién tiene la responsabilidad de la seguridad de la unidad o establecimiento?",
        "opciones": ["El personal de guardia únicamente.", "El comandante o director de la unidad o establecimiento.", "El jefe de seguridad solamente.", "El oficial de día."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué es la 'Fuerza de Reacción Inmediata'?",
        "opciones": ["Un grupo de personal administrativo.", "Un recurso humano para garantizar la seguridad de las unidades y establecimientos navales.", "Un equipo de mantenimiento.", "Un comité de bienvenida."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué se considera una amenaza común a la seguridad física, relacionada con el personal?",
        "opciones": ["La cooptación de personal por parte de la Delincuencia Organizada.", "El incremento de la moral del personal.", "La buena conducta.", "La alta participación en eventos sociales."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Cuál es un punto vulnerable común relacionado con la infraestructura?",
        "opciones": ["Las áreas de juego.", "Puertas y/o portones perimetrales en mal estado y/o sin vigilancia.", "Las oficinas de reclutamiento.", "Los comedores."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué implica la delimitación de Áreas Restringidas?",
        "opciones": ["Crear zonas de libre acceso.", "Clasificarlas conforme a las políticas generales de seguridad de la información de la Secretaría de Marina.", "Eliminar cualquier tipo de control.", "Permite el tránsito sin supervisión."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué deben hacer los visitantes en las instalaciones navales?",
        "opciones": ["Moverse libremente sin supervisión.", "Ser acompañados permanentemente por personal naval de guardia.", "Solo esperar en la entrada.", "Ir directamente a su destino sin registrarse."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se debe verificar sobre los servicios de paquetería y mensajería al recibir paquetes?",
        "opciones": ["Si son servicios nuevos.", "Que sean conocidos y utilicen preferentemente uniformes y vehículos oficiales, exigiendo identificación oficial y de la empresa.", "Si el paquete es grande o pequeño.", "Si la entrega es gratuita."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué busca el alumbrado en las instalaciones?",
        "opciones": ["Generar un ambiente oscuro.", "Obtener un nivel de iluminación óptimo en una función específica.", "Reducir la visibilidad.", "Crear sombras para la estética."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué función tienen los sistemas de vigilancia de circuito cerrado?",
        "opciones": ["Reemplazar al personal de seguridad.", "Medios auxiliares a la función de los vigilantes.", "Generar ingresos adicionales.", "Ofrecer entretenimiento al personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué debe incluir la constitución de la guardia en prevención?",
        "opciones": ["Solo el jefe de guardia.", "Personal naval de los diferentes cuerpos y servicios capacitados y adiestrados para la vigilancia y/o defensa.", "Solo personal civil.", "Personal administrativo."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es la importancia de la aplicación y supervisión de los Planes de Contingencias?",
        "opciones": ["Son opcionales y no obligatorios.", "Reducir al mínimo los efectos de un desastre de gran proporción que resulte de causas naturales o antropogénicas.", "Aumentar la burocracia.", "Generar confusión."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué incluye el concepto de Cultura de Seguridad?",
        "opciones": ["Solo las reglas escritas.", "Las actitudes y valores del personal de la Secretaría de Marina Armada de México de manera institucional en los aspectos relativos a la seguridad física.", "El entretenimiento del personal.", "La elección de uniformes."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué sucede si la cultura de seguridad física se observa fuerte?",
        "opciones": ["Hay menos necesidad de entrenamiento.", "Se traduce en una fortaleza de seguridad institucional.", "El personal se relaja.", "No hay impacto en la seguridad."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Cuál es la meta de un programa de educación en cultura de seguridad física?",
        "opciones": ["Limitar el conocimiento al personal superior.", "Familiarizar y concientizar a todo el personal naval sobre la importancia de la adopción de medidas de seguridad.", "Reducir las horas de trabajo.", "Evitar la comunicación entre el personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Quién es el responsable de la implementación del programa de seguridad física?",
        "opciones": ["El Comandante o Director de la instalación naval.", "El jefe de seguridad.", "El personal de tropa.", "El Oficial de Vigilancia."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué tipo de evaluación se realiza como parte del programa de seguridad física?",
        "opciones": ["Evaluación del personal de limpieza.", "Evaluación del programa, los instructores y el personal naval participante.", "Evaluación de los alimentos.", "Evaluación de los vehículos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué se debe mantener actualizado en relación con la seguridad física, según las funciones del Jefe de Seguridad?",
        "opciones": ["La lista de correos electrónicos.", "La agenda de riesgo de la Unidad.", "Los datos personales de cada miembro.", "Los registros de asistencia a eventos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué se busca asegurar con la aplicación de la legislación vigente y la normatividad emitida por el Estado Mayor General de la Armada?",
        "opciones": ["El buen funcionamiento de todos los procesos, directivas y recomendaciones en materia de seguridad.", "La flexibilidad de las operaciones.", "El cumplimiento de las vacaciones.", "La expansión de las instalaciones."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué se incluye en el registro de prácticas de los zafarranchos para la mejora continua?",
        "opciones": ["Solo el tiempo de respuesta.", "Memoria fotográfica, observaciones y recomendaciones.", "Nombres de los participantes.", "Fechas de futuras prácticas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué es la seguridad física según su concepto?",
        "opciones": ["Acciones para el bienestar personal.", "Medidas que se adoptan para evitar lesión o pérdidas de vidas, daño, desorganización, destrucción de bienes muebles e inmuebles de la nación.", "Estrategias de comunicación.", "Gestión de recursos financieros."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué debe incluir el planeamiento de seguridad?",
        "opciones": ["Solo la situación económica.", "Decisiones que dependen del tamaño y naturaleza, misión, vulnerabilidad, ubicación geográfica, situación económica y política del área, factibilidad de apoyo externo, capacidades propias y del enemigo o trasgresor de la ley.", "Únicamente el número de personal.", "El color de las instalaciones."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué sucede con los recursos humanos y materiales en la seguridad física?",
        "opciones": ["Son elementos independientes.", "Los elementos de la seguridad física de las unidades y establecimientos se dividen en recursos humanos y materiales.", "Se utilizan indistintamente.", "Son intercambiables."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué papel juegan las barreras perimétricas?",
        "opciones": ["Solo como adorno.", "Definen los límites físicos de un área protegida y restringen o impiden el acceso a personas en áreas no autorizadas.", "Facilitan el acceso.", "Proveen sombra."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es el propósito del control de accesos, además de permitir la entrada a personal autorizado?",
        "opciones": ["Medir el nivel de ruido.", "Evitar la introducción de dispositivos o componentes perjudiciales, la fuga de información y la malversación o robo de material o equipo.", "Contar la cantidad de visitantes.", "Controlar la temperatura del aire."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué debe ser el diseño de un gafete o tarjetón?",
        "opciones": ["Fácil de alterar.", "Que represente máxima dificultad a cualquier intento para alterarlo o reproducirlo.", "Simple y sin información.", "Que pueda ser duplicado fácilmente."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué puede invalidar el sistema más sofisticado de seguridad en el reconocimiento del personal?",
        "opciones": ["La desidia o apatía por parte del personal de guardia para comparar al portador con la credencial de identidad mostrada.", "La tecnología avanzada.", "El número de personal.", "La calidad del uniforme."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué sistema de comunicación debe existir para cada unidad o establecimiento naval?",
        "opciones": ["Uno solo para toda la Secretaría.", "Un plan táctico simplificado de comunicaciones.", "Un sistema de comunicación social.", "Un sistema de comunicación para entretenimiento."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué tipo de planes de contingencia son básicos para una unidad o establecimiento naval?",
        "opciones": ["Plan de Contratación.", "Plan de Defensa, Plan de Contraincendio, Plan de Evacuación.", "Plan de Finanzas.", "Plan de Recursos Humanos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué significa que la cultura de seguridad física se percibe como la conducta observada en cada uno de los miembros de la Secretaría de Marina Armada de México?",
        "opciones": ["Que es una responsabilidad individual solamente.", "Que se ve como un todo institucional, sin considerar la individualidad de las personas.", "Que solo aplica al personal de alto rango.", "Que es irrelevante para la seguridad."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué requiere la imagen pública y el prestigio institucional de la Secretaría de Marina - Armada de México?",
        "opciones": ["Menos medidas de seguridad.", "La adopción de una cultura de seguridad física que impulse la sinergia necesaria para responder a las amenazas actuales.", "Un cambio de nombre.", "La reducción de personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué genera el programa continuo y obligatorio de educación en seguridad física?",
        "opciones": ["Confusión.", "La unificación de la conciencia que la seguridad física exitosa demanda.", "División.", "Desinterés."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Quiénes deben estar capacitados para interpretar el lenguaje corporal que denote amenazas en los sistemas de vigilancia de circuito cerrado?",
        "opciones": ["El personal administrativo.", "El personal de monitoreo.", "El personal de cocina.", "El personal de mantenimiento."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué objetivo tiene el planeamiento de seguridad para las instalaciones?",
        "opciones": ["Ahorrar recursos.", "Asegurar un eficiente proceso de planeación y ejecución de las acciones tendientes a garantizar la seguridad.", "Decorar las instalaciones.", "Crear confusión."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Cuál es la función del Jefe de Seguridad según el ANEXO 'A'?",
        "opciones": ["Gestionar el presupuesto.", "Asesorar al mando y mantenerlo informado en todo lo relacionado con la seguridad física de las Instalaciones navales.", "Planificar eventos sociales.", "Organizar actividades deportivas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué busca prevenir y controlar la protección física?",
        "opciones": ["Solo los daños a la propiedad.", "Los riesgos hacia los recursos humanos, materiales y financieros.", "La pérdida de tiempo.", "La falta de comunicación."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué es la 'Fuga de información' una amenaza común a la seguridad física?",
        "opciones": ["No, es una vulnerabilidad.", "Sí, es una amenaza común.", "Es un riesgo natural.", "Es una medida de protección."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Qué tipo de fenómenos se mencionan como amenazas a la seguridad física?",
        "opciones": ["Fenómenos culturales.", "Fenómenos hidrometeorológicos.", "Fenómenos sociales.", "Fenómenos económicos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Qué ocurre cuando hay una debilidad del sistema de control y confianza institucional?",
        "opciones": ["Aumenta la seguridad.", "Se convierte en una vulnerabilidad común a la seguridad física.", "No afecta la seguridad.", "Mejora el rendimiento del personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Qué papel juega el Comandante o Director en el programa de seguridad física?",
        "opciones": ["Debe tener voluntad y apoyo directo.", "Solo aprueba el presupuesto.", "No tiene participación.", "Solo supervisa una vez al año."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué es importante registrar sobre las prácticas de zafarranchos?",
        "opciones": ["Solo la asistencia del personal.", "La memoria fotográfica, observaciones y recomendaciones para la mejora continua.", "Los nombres de los observadores externos.", "El tipo de equipo utilizado."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Cuál es uno de los propósitos de la delimitación de áreas restringidas?",
        "opciones": ["Crear áreas de esparcimiento.", "Determinar las áreas restringidas con base en un análisis de riesgo.", "Aumentar el tráfico de personas.", "Facilitar el acceso a personal no autorizado."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },

    # Bloque 6 de 6: Preguntas 251-300
    {
        "pregunta": "¿Qué tipo de planes deben considerar todo el efectivo de la unidad o establecimiento naval en una acción conjunta para combatir la amenaza común?",
        "opciones": ["Planes de entretenimiento.", "Planes de contingencia.", "Planes de desarrollo profesional.", "Planes de celebración."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se traduce en una fortaleza de seguridad institucional?",
        "opciones": ["Una cultura de seguridad física fuerte.", "El aumento del personal.", "La cantidad de equipo disponible.", "La implementación de nuevas tecnologías únicamente."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Cuál es la responsabilidad compartida por todos los miembros de la Secretaría de Marina - Armada de México en seguridad física?",
        "opciones": ["La limpieza de las instalaciones.", "Descubrir y frustrar planes o acciones en contra de la seguridad física de las unidades y establecimientos navales.", "Organizar eventos sociales.", "Administrar los recursos financieros."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué garantiza un programa continuo y obligatorio de educación en seguridad física?",
        "opciones": ["La desinformación.", "El desarrollo de la cultura de seguridad física.", "La inactividad del personal.", "La reducción de la eficiencia."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué se debe evaluar en el programa de seguridad física para una retroalimentación que permita la mejora continua?",
        "opciones": ["Solo el equipo.", "El programa, los instructores y el personal naval participante.", "Las instalaciones físicas.", "Los vehículos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué medios gráficos se utilizan para la sublimidad del mensaje en cultura de seguridad?",
        "opciones": ["Audios y videos solamente.", "Cartelones, lonas y folletos.", "Mensajes de texto.", "Correo electrónico."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "Según el ANEXO 'A', ¿qué debe hacer el Jefe de Seguridad con los procesos críticos en su área de responsabilidad?",
        "opciones": ["Ignorarlos.", "Identificarlos y aplicar las metodologías establecidas por la CSI para realizar análisis de riesgo y administrar las vulnerabilidades y fortalezas de los sistemas de información.", "Delegarlos por completo.", "Eliminarlos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué tipo de agenda debe mantener actualizada el Jefe de Seguridad?",
        "opciones": ["Agenda de reuniones.", "Agenda de riesgo de la Unidad.", "Agenda personal.", "Agenda de contactos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué implica la aplicación continua del Plan de Contingencias por medio de zafarranchos?",
        "opciones": ["Una actividad recreativa.", "Garantizar el pleno conocimiento por todo el personal naval.", "La reducción de entrenamiento.", "Un evento opcional."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Quiénes asumen roles importantes durante la implementación de los planes de seguridad y contingencia para preservar los recursos humanos, materiales y financieros de la instalación naval?",
        "opciones": ["Solo la guardia en prevención.", "Ambas guardias (de armas y de apoyo).", "El personal administrativo.", "Los proveedores externos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué factores componen el riesgo, según el documento?",
        "opciones": ["Solo la ubicación geográfica.", "La amenaza y la vulnerabilidad.", "El tamaño de la unidad.", "El número de personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué es un ejemplo de riesgo antropogénico?",
        "opciones": ["Terremoto.", "Descuidos humanos que resultan en daño, pérdida o comprometimiento.", "Tsunami.", "Tormenta."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué son los estudios de estado mayor para el planeamiento de seguridad?",
        "opciones": ["Instrumentos opcionales.", "Instrumentos indispensables para asegurar un eficiente proceso de planeación y ejecución de las acciones.", "Solo documentos históricos.", "Registros de personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Quiénes son algunos de los recursos humanos para la seguridad de las unidades y establecimientos navales?",
        "opciones": ["Personal de cocina.", "Jefe de seguridad, Oficial de Vigilancia, Oficial de Cuartel, Oficial de Día, Guardia en Prevención, Fuerza de Reacción Inmediata.", "Personal de limpieza.", "Personal de enfermería."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué permiten las edificaciones de Sala de Guardia y Puestos de Vigilancia?",
        "opciones": ["Almacenar equipo no utilizado.", "Alojar o establecer al personal de guardia para ser empleados de manera inmediata en caso de una situación contingente.", "Realizar eventos sociales.", "Servir como áreas de descanso prolongado."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué incluye el registro y control para la seguridad física, en relación con el personal?",
        "opciones": ["Identificación del personal naval con credencial de alta seguridad.", "Registro de visitantes sin identificación.", "Registro de preferencias personales.", "Registro de actividades de ocio."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué ocurre al encontrarse puntos o áreas débiles en el sistema de seguridad física de las instalaciones navales?",
        "opciones": ["Disminuyen los riesgos.", "Se maximizan los riesgos de acuerdo a las amenazas existentes.", "No hay impacto en la seguridad.", "Se mejora la eficiencia."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Cuál es una vulnerabilidad común a la seguridad física relacionada con el control?",
        "opciones": ["Falta de controles y registro de entrada y salida de material.", "Exceso de controles.", "Demasiado registro de información.", "Control sin supervisión."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Qué implica el Concepto de Protección Física?",
        "opciones": ["Solo la gestión de recursos.", "El conjunto de políticas y medidas para mejorar la seguridad física y prevenir riesgos.", "La creación de nuevos riesgos.", "La desorganización de las unidades."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se implementa para minimizar los riesgos a la seguridad física de las unidades y establecimientos navales?",
        "opciones": ["Solo planes de contingencia.", "Medidas de Protección Física.", "Procesos administrativos.", "Actividades recreativas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué deben hacer las barreras perimétricas en relación con el acceso de un intruso?",
        "opciones": ["Facilitar su paso.", "Obstaculizar y demorar el acceso.", "Ignorar su presencia.", "Atraerlos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué son normalmente las Comandancias o Direcciones en el contexto de áreas vulnerables?",
        "opciones": ["Puntos de reunión.", "Áreas vulnerables.", "Zonas de libre acceso.", "Lugares de descanso."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué clasificación de área tiene máxima seguridad y control?",
        "opciones": ["Área Negra.", "Área Blanca.", "Área Gris.", "Área Verde."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se debe implementar para todo el personal que labora en las áreas restringidas?",
        "opciones": ["Uso de uniformes de colores específicos.", "Uso de identificación.", "Acceso sin revisión.", "Prohibición de acceso."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué es uno de los requisitos para la acreditación del personal en las Áreas Blancas?",
        "opciones": ["Un acuerdo de confidencialidad sin validez.", "Un Acuerdo de no revelación de información.", "Una carta de recomendación de un amigo.", "Un permiso verbal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué ocurre si el personal de guardia muestra desidia o apatía al comparar al portador con la credencial de identidad mostrada?",
        "opciones": ["Mejora la seguridad.", "Puede invalidar al sistema más sofisticado de seguridad.", "No tiene ningún efecto.", "Agiliza el proceso."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cómo deben ser los gafetes para visitantes?",
        "opciones": ["Pequeños y difíciles de ver.", "De fácil identificación tanto por tamaño como por color.", "Indistinguibles del personal.", "Sin información visible."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué debe hacer el jefe de seguridad con los contratistas?",
        "opciones": ["Permitirles acceso libre a todas las áreas.", "Mostrarles las áreas permitidas y las estrictamente restringidas.", "Ignorar su presencia.", "Dejarlos trabajar sin supervisión."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se debe hacer con la entrada y salida de paquetes?",
        "opciones": ["Permitirlas sin inspección.", "No permitir la entrada ni salida de paquetes sin previa inspección y autorización.", "Solo inspeccionar paquetes grandes.", "Permitir solo la entrada sin inspección."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Dónde deben estar alejadas las áreas de estacionamiento de vehículos privados?",
        "opciones": ["Cerca de la entrada principal.", "De un área en la que pudiera causar daños o pérdidas de vidas por explosión.", "Dentro de los edificios.", "En cualquier lugar conveniente."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué debe considerarse para el alumbrado de emergencia?",
        "opciones": ["Un sistema que solo funcione con luz solar.", "Un sistema que pueda suplir los sistemas de iluminación continua durante fallas eléctricas.", "Luces decorativas.", "Un sistema que solo funcione manualmente."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué debe garantizar el establecimiento de la guardia en prevención?",
        "opciones": ["Solo el orden interno.", "El control efectivo de la fuerza de guardia y una seguridad adecuada a las actividades y funciones principales.", "La reducción de personal.", "La minimización de las tareas."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué debe incluir el mayor número de ordenamientos para las consignas de los servicios de guardia?",
        "opciones": ["Información personal del personal.", "Detalles de sus vacaciones.", "Para garantizar la ejecución del servicio de guardia de forma eficiente y efectiva.", "Opiniones personales."],
        "respuesta_correcta": 2, # Changed from 1 based on specific wording check
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Para qué se utilizan las señales audibles y visibles?",
        "opciones": ["Para crear ruido.", "Activar un plan de zafarrancho facilitando la comunicación instantánea.", "Como medios de entretenimiento.", "Para indicar la hora."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué deben considerar los planes de contingencia para su ejecución?",
        "opciones": ["Solo el horario nocturno.", "Horario laborable (todo el personal presente) y en horario no laborable (solo personal de guardia).", "Solo los fines de semana.", "Solo los días festivos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué es la 'idiosincrasia de la responsabilidad individual' que la cultura de seguridad física busca transformar?",
        "opciones": ["Un pensamiento grupal.", "La creencia de que solo el personal de guardia es responsable de la seguridad.", "La idea de que la seguridad es opcional.", "La preferencia por el trabajo solitario."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué garantiza la 'unificación de la conciencia' en seguridad física?",
        "opciones": ["Que la seguridad física exitosa demanda.", "La división del personal.", "La ineficiencia en las operaciones.", "La falta de compromiso."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué es uno de los requerimientos mínimos de un programa eficaz de seguridad física?",
        "opciones": ["Voluntad y apoyo directo del Comandante o Director de la instalación naval.", "Ignorar las sugerencias del personal.", "Reducir la capacitación.", "Descartar la evaluación."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué se recomienda para que toda propuesta de cambio en el modelo doctrinario asegure su comprensión y mejor valoración?",
        "opciones": ["Citación específica del término y concepto, y las razones que lo fundamentan.", "Solo la opinión personal.", "Un formato libre.", "Un resumen muy breve."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "¿Cuál es el objetivo de este manual en relación con la seguridad de las unidades y establecimientos navales?",
        "opciones": ["Solo responder a incidentes.", "Orientar y normar la actuación del personal para proporcionar la seguridad, considerando la prevención y/o respuestas a situaciones que pudieran ocasionar la pérdida o daño de recursos.", "Exclusivamente prevenir daños materiales.", "Informar sobre la pérdida de recursos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Introducción"
    },
    {
        "pregunta": "¿Qué debe incluir el diseño de un gafete para representar máxima dificultad a cualquier intento de alteración o reproducción?",
        "opciones": ["Solo el nombre del portador.", "Debe ser rubricado por el Comandante o Director.", "Un código de barras simple.", "Un diseño genérico."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Qué se debe hacer con las consignas de los servicios de guardia para garantizar una seguridad óptima?",
        "opciones": ["Dejarlas sin cambios.", "Redactarlas de manera sencilla y revisarlas y actualizarlas periódicamente.", "Mantenerlas complejas.", "Cambiarlas diariamente."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es el propósito de la meta de un programa de educación en relación a la cultura de seguridad física?",
        "opciones": ["Desmotivar al personal.", "Familiarizar y concientizar a todo el personal naval sobre la importancia de la adopción de medidas de seguridad.", "Aumentar la burocracia.", "Reducir la participación del personal."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Por qué es necesario un programa continuo y obligatorio de educación en seguridad física?",
        "opciones": ["Para que el personal olvide las directrices.", "Para garantizar el desarrollo de la cultura de seguridad física.", "Para reducir la inversión en seguridad.", "Para aumentar la confusión."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "¿Qué se menciona en el ANEXO 'B' como parte de la 'Lista de Verificación para la Seguridad Física de las Instalaciones Navales'?",
        "opciones": ["Plan de Marketing.", "Plan de Cultura de Seguridad.", "Plan de Ventas.", "Plan de Recursos Humanos."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué expedientes se incluyen en la lista de verificación del ANEXO 'B' relacionados con el Jefe de Seguridad?",
        "opciones": ["Expediente de informes recibidos referente a la Seguridad Física y expediente de acciones y respuestas dadas.", "Expediente de gastos personales.", "Expediente de quejas sin seguimiento.", "Expediente de sugerencias sin implementación."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Anexos"
    },
    {
        "pregunta": "¿Qué se busca evitar con la seguridad física de las unidades y establecimientos?",
        "opciones": ["La pérdida de recursos humanos, materiales y financieros.", "La eficiencia operativa.", "El crecimiento institucional.", "La adquisición de nuevos equipos."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "¿Qué se considera una vulnerabilidad común relacionada con el manejo de la información clasificada?",
        "opciones": ["Descuido en el manejo de información clasificada.", "Riguroso control de la información.", "Acceso ilimitado a la información.", "Compartir información libremente."],
        "respuesta_correcta": 0,
        "dificultad": "facil",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "¿Qué es un 'Área Gris' según la clasificación de áreas de seguridad?",
        "opciones": ["Área con máxima seguridad.", "Área con acceso restringido y control moderado.", "Área de libre tránsito.", "Área sin medidas de seguridad."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "¿Cuál es la función del alumbrado para los vigilantes?",
        "opciones": ["Deslumbrarlos.", "Formar un mínimo de sombras y un mínimo de resplandor en los ojos de los vigilantes.", "Crear áreas oscuras para que se escondan.", "Eliminar toda visibilidad."],
        "respuesta_correcta": 1,
        "dificultad": "facil",
        "tema": "Capítulo III. Protección Física"
    },

    # Bloque Bonus: Preguntas 301-350 (Nivel Dios - Razonamiento)
    {
        "pregunta": "Si un Comandante de Unidad decide delegar completamente la responsabilidad de la seguridad física a su Jefe de Seguridad sin supervisión ni apoyo directo, ¿qué impacto podría tener esta acción en la efectividad del programa de seguridad física de la instalación, según el manual?",
        "opciones": ["El programa sería más eficiente debido a la autonomía del Jefe de Seguridad.", "El programa sería robusto, ya que el Jefe de Seguridad tomaría todas las decisiones.", "El programa podría ser ineficaz, ya que la 'voluntad y apoyo directo del Comandante o Director' es un requerimiento mínimo para un programa eficaz.", "No habría impacto, ya que la responsabilidad recae en el Jefe de Seguridad por nombramiento."],
        "respuesta_correcta": 2,
        "dificultad": "dios",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "El manual establece que el conocimiento del modelo doctrinario 'norma las características, procedimientos, equipo y material empleado para la seguridad de las instalaciones navales'. ¿Cómo se relaciona esto con la capacidad del personal naval para prevenir incidentes que afecten la integridad física del personal y la conservación del material?",
        "opciones": ["El conocimiento del modelo es secundario; la experiencia práctica es lo único que importa.", "Al normar estos elementos, el conocimiento auxiliará al personal para prevenir cualquier incidente.", "La normatividad solo es útil para la auditoría, no para la prevención.", "No hay una relación directa entre el conocimiento de las normas y la prevención de incidentes."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "Dada la clasificación de riesgos en 'Naturales y Antropogénicos', y el hecho de que una 'Inundación' puede ser causada por acción humana, ¿qué implicación tiene esto para el planeamiento de seguridad en una Unidad Naval ubicada cerca de un río con represas controladas por el hombre?",
        "opciones": ["Solo se debe considerar como riesgo natural, ya que su origen es el agua.", "Debe analizarse tanto como riesgo natural (por fenómenos meteorológicos) como antropogénico (por fallas o manipulación de la represa) para una planificación completa.", "Solo se debe planificar para un posible 'Terremoto', ya que es el riesgo más grave.", "No es necesario un planeamiento específico, ya que la inundación es poco probable."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "El documento menciona que los riesgos antropogénicos incluyen 'Descuidos Humanos que resultan en daño, pérdida o comprometimiento'. Si un miembro del personal olvida cerrar con llave un almacén de material clasificado, ¿cómo se clasificaría este evento y qué vulnerabilidad podría haber contribuido a ello?",
        "opciones": ["Sería un riesgo natural, y la vulnerabilidad sería la falta de personal.", "Sería un riesgo antropogénico (por descuido humano), y la 'Apatía para la supervisión de material clasificado' o 'Falta de controles y registro de entrada y salida de material' podrían ser vulnerabilidades contribuyentes.", "Sería un riesgo de seguridad, pero sin vulnerabilidad asociada.", "Sería un incidente menor sin clasificación de riesgo."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física / Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "El manual indica que 'Al existir cambios estructurales o tecnológicos que afecten a la seguridad de las unidades y establecimientos es necesario revisar y actualizar la planificación de seguridad física'. Si una Unidad Naval instala un nuevo sistema de control de acceso biométrico, ¿qué acción es esencial y por qué, más allá de la instalación del equipo?",
        "opciones": ["Es esencial no hacer cambios en la planificación para mantener la estabilidad.", "Es esencial revisar y actualizar la planificación de seguridad física para integrar el nuevo sistema y asegurar su eficiencia y efectividad.", "Solo es necesario capacitar al personal que operará el sistema, sin actualizar la planificación.", "No es necesario hacer nada, el nuevo sistema se adapta automáticamente."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "Considerando que la 'Fuerza de Reacción Inmediata' es un recurso humano, y que la vigilancia con circuito cerrado debe ser 'respaldada por una Fuerza de Reacción que actúe en caso de detectarse situaciones de amenaza', ¿qué implica esto para la eficacia de un sistema de circuito cerrado sin una fuerza de reacción adecuada?",
        "opciones": ["El sistema de circuito cerrado sería igualmente eficaz, ya que es tecnológico.", "La vigilancia con circuito cerrado sin una fuerza de reacción adecuada sería limitada en su capacidad de respuesta y contención de amenazas.", "El sistema de circuito cerrado solo serviría para la recopilación de pruebas, no para la acción inmediata.", "La fuerza de reacción solo es necesaria para amenazas de gran escala."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física / Capítulo III. Protección Física"
    },
    {
        "pregunta": "El documento enfatiza que 'la desidia o apatía por parte del personal de guardia para comparar al portador con la credencial de identidad mostrada, puede invalidar al sistema más sofisticado de seguridad'. Si una Unidad Naval invierte en gafetes de alta seguridad con múltiples elementos de autenticación, ¿cuál es el factor crítico para el éxito del sistema y por qué?",
        "opciones": ["La sofisticación del gafete es el factor crítico, ya que la tecnología es infalible.", "La estricta aplicación y supervisión por parte del personal de guardia es el factor crítico, ya que la apatía puede anular la inversión tecnológica.", "El factor crítico es la rapidez del proceso de verificación, no la comparación.", "La cantidad de gafetes emitidos es el factor crítico para la seguridad."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "El manual clasifica las áreas en 'Blanca', 'Gris' y 'Negra'. Si se detecta a un contratista trabajando en un 'Área Blanca' sin la acreditación y supervisión adecuadas, ¿qué tipo de riesgo de seguridad se materializa y por qué su presencia en esta área es particularmente crítica?",
        "opciones": ["Sería un riesgo natural, sin especial criticidad en el Área Blanca.", "Se materializa un riesgo antropogénico (posible infiltración o descuido). Es crítico porque el 'Área Blanca' es de 'máxima seguridad y control' y resguarda información o material clasificado.", "No es un riesgo de seguridad, solo un incumplimiento administrativo.", "Es un riesgo de reputación, no físico."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "El documento señala que el alumbrado debe 'formar un mínimo de sombras y un mínimo de resplandor en los ojos de los vigilantes'. Si un sistema de iluminación es diseñado sin considerar esta directriz, ¿qué consecuencia directa podría tener en la efectividad de la vigilancia nocturna y la capacidad de detección de intrusos?",
        "opciones": ["Aumentaría la visibilidad general, mejorando la detección.", "La presencia de sombras excesivas podría ofrecer cobertura a intrusos, y el resplandor podría cegar temporalmente a los vigilantes, reduciendo su capacidad de detección.", "No tendría ningún impacto en la efectividad, ya que el alumbrado es solo una disuasión pasiva.", "Haría que la visibilidad fuera más dramática, lo cual es bueno para la seguridad."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "La 'cultura de seguridad física' se percibe como la 'conducta observada en cada uno de los miembros de la Secretaría de Marina Armada de México como un todo institucional'. Si un miembro del personal ignora constantemente las consignas de seguridad, ¿qué impacto tiene esta conducta individual en la fortaleza de seguridad institucional, según el manual?",
        "opciones": ["No hay impacto, ya que es una acción individual y la fortaleza es institucional.", "Esta conducta individual puede sumarse a otros 'eventos aislados' para 'deteriorar o disminuir esa fortaleza de seguridad institucional'.", "Mejora la flexibilidad del sistema de seguridad.", "Solo afecta la reputación personal del individuo."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "El manual establece que el objetivo de la cultura de seguridad física es transformar la 'idiosincrasia de la responsabilidad individual del personal naval que se encuentra de guardia a un pensamiento doctrinario en donde todos los integrantes somos responsables de la seguridad física de las instalaciones navales, aún sin estar nombrado en el servicio de guardia'. ¿Qué beneficio fundamental se espera de esta transformación para la seguridad de la institución?",
        "opciones": ["Reducir la cantidad de personal necesario para la guardia.", "Crear una 'sinergia necesaria' y una 'unificación de la conciencia' donde cada miembro actúa como un sensor y una barrera activa contra las amenazas, fortaleciendo la seguridad general.", "Limitar la responsabilidad a solo unos pocos individuos clave.", "Facilitar la delegación de tareas administrativas al personal de seguridad."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "El ANEXO 'A' asigna al Jefe de Seguridad la función de 'Identificar los procesos críticos en su área de responsabilidad y aplicar las metodologías establecidas por la CSI para realizar análisis de riesgo y administrar las vulnerabilidades y fortalezas de los sistemas de información'. Si el Jefe de Seguridad solo se enfoca en las amenazas visibles sin un análisis profundo de los procesos, ¿qué consecuencia podría tener esto en la gestión de la seguridad?",
        "opciones": ["La seguridad sería más reactiva que preventiva.", "Podría llevar a una 'deficiencia de la cultura de prevención y seguridad' y dejar vulnerabilidades críticas sin abordar, ya que no se comprenderían las debilidades internas del sistema.", "Se optimizarían los recursos al evitar análisis complejos.", "No tendría mayor impacto, ya que las amenazas son siempre obvias."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Anexos"
    },
    {
        "pregunta": "El documento subraya la importancia de 'revisar y actualizar la planificación de seguridad física' ante cambios estructurales o tecnológicos. Si una Unidad Naval decide implementar una reestructuración interna significativa que altera la disposición de sus oficinas y almacenes, pero no revisa su plan de seguridad, ¿qué riesgo concreto se introduce?",
        "opciones": ["El riesgo de obsolescencia del equipo de oficina.", "El riesgo de que la planificación existente ya no sea 'eficiente' o 'eficaz' para garantizar la seguridad en la nueva configuración, lo que podría crear nuevos 'puntos y áreas vulnerables'.", "El riesgo de que el personal se sienta incómodo con los nuevos espacios.", "El riesgo de exceder el presupuesto."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "En el capítulo de 'Protección Física' se menciona la 'Aplicación y supervisión de los planes de contingencias'. Si una Unidad Naval tiene planes de contingencia, pero nunca los practica ('zafarranchos'), ¿qué impacto real tiene esta omisión en la capacidad de respuesta ante una emergencia, a pesar de tener los planes en papel?",
        "opciones": ["Los planes serían igual de efectivos, ya que están escritos.", "La omisión de prácticas impediría 'detectar inconsistencias, aplicar mejoras a los planes y familiarizar al personal naval en la ejecución', lo que podría llevar a una 'reacción rapida y eficaz' deficiente o nula en una situación real.", "La falta de práctica solo afecta el tiempo de respuesta, no la eficacia.", "Ahorra tiempo y recursos al no realizar simulacros."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "La identificación y evaluación de 'puntos y áreas vulnerables' se realiza durante el 'análisis de riesgos'. Si una Unidad Naval solo se enfoca en las áreas perimetrales sin considerar los puntos internos como 'Alcantarillas de los ductos de aguas negras o grises que cruzan las instalaciones' o 'Plantas motogeneradoras de energia eléctricas', ¿qué tipo de vulnerabilidad podría persistir sin ser abordada?",
        "opciones": ["Una vulnerabilidad relacionada únicamente con desastres naturales.", "Una vulnerabilidad interna crítica que podría ser explotada por 'Actos intencionales de comisión u omisión' o 'Descuido en el manejo de información clasificada', afectando directamente 'activos prioritarios'.", "Una vulnerabilidad estética que no afecta la seguridad real.", "Una vulnerabilidad que solo afectaría el suministro de agua."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "Si el Jefe de Seguridad no informa 'al Mando sobre los accesos no autorizados a las instalaciones o el incumplimiento de directivas', ¿qué posible consecuencia institucional, más allá del incidente inmediato, podría surgir en relación con la 'fortaleza de seguridad institucional'?",
        "opciones": ["No habría consecuencias, ya que la seguridad es una responsabilidad del Jefe de Seguridad.", "La falta de información oportuna al Mando podría impedir la aplicación de 'sanciones correspondientes', y al no abordar estas fallas sistémicamente, podría erosionar la 'fortaleza de seguridad institucional' y la 'cultura de seguridad'.", "El Mando se mantendría al tanto de forma independiente.", "Solo afectaría la moral del personal de guardia."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Anexos"
    },
    {
        "pregunta": "El manual indica que los estudios de estado mayor son 'instrumentos indispensables' para asegurar un 'eficiente proceso de planeación y ejecución de las acciones' de seguridad. Si un Comandante decide basar su planeamiento de seguridad únicamente en la experiencia pasada y en el 'sentido común' sin realizar estos estudios, ¿qué riesgo intrínseco asume para la seguridad de su Unidad?",
        "opciones": ["No asume ningún riesgo, ya que la experiencia es el mejor maestro.", "Asume el riesgo de una 'deficiencia de la cultura de prevención y seguridad' y de una planificación ineficiente o incompleta que no considera todos los factores y vulnerabilidades actuales.", "El riesgo de sobreplanificación.", "El riesgo de invertir demasiado en seguridad."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "El Concepto de Seguridad Física busca 'hacer todo lo necesario para que estos [recursos] existan, se desarrollen y cumplan los propósitos fijados'. Si una Unidad Naval sufre repetidos robos 'hormiga' de material sin una respuesta efectiva, ¿cómo impacta esto en la capacidad de los recursos para cumplir sus propósitos, a pesar de que el daño individual pueda parecer menor?",
        "opciones": ["No hay impacto, ya que es 'robo hormiga'.", "La acumulación de pérdidas por 'robo hormiga', aunque individualmente pequeña, eventualmente 'causaran desorganización y la pérdida de la eficiencia y efectividad en el cumplimiento de la misión' de la Unidad.", "El impacto es solo financiero, no operativo.", "El cumplimiento de los propósitos se mantiene inalterado."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física / Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "El documento menciona que los 'Órganos de reclutamiento carentes de plataformas de investigación del personal' son una vulnerabilidad. Si se descubre que un nuevo miembro del personal, reclutado bajo estas circunstancias, está involucrado en 'Fuga de información', ¿qué amenaza se materializó y cuál fue la causa raíz de esta vulnerabilidad?",
        "opciones": ["La amenaza fue 'Robo de material clasificado', causada por falta de cámaras.", "La amenaza fue 'Fuga de información' y la causa raíz de la vulnerabilidad fue la 'Debilidad del sistema de control y confianza institucional' y la 'carencia de plataformas de investigación del personal' en el reclutamiento.", "La amenaza fue un riesgo natural, sin relación con el reclutamiento.", "La amenaza fue la 'Intervención de señales de radio', y la causa fue la antigüedad del equipo."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "La 'Sublimidad del Mensaje' sugiere la 'observación repetida de mensajes colocados en cartelones, lonas y folletos' para inculcar el aprendizaje sobre seguridad. Si estos recursos gráficos se colocan en lugares poco visibles o de acceso restringido, ¿qué impacto tendrá en la 'concientización general' del personal?",
        "opciones": ["Aumentará la concientización debido a la exclusividad de la información.", "La concientización general será limitada o nula, ya que el mensaje no llegará a 'todo el personal' y no se logrará la 'fácil comprensión de la importancia de la seguridad'.", "La concientización se dará a través de otros medios automáticamente.", "Solo afectará a un pequeño grupo de personal, no a la concientización general."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "Si un Oficial de Guardia en Prevención, ante una 'amenaza que supere la capacidad de respuesta de la fuerza propia', decide no solicitar apoyo a la Fuerza de Reacción Inmediata por considerar que 'puede manejarlo', ¿qué consecuencia potencial podría surgir en el contexto de la 'preservación de los recursos humanos, materiales y financieros'?",
        "opciones": ["No habría consecuencia, ya que demuestra liderazgo.", "Podría resultar en la 'pérdida o daño de recursos humanos, materiales y financieros', ya que se está omitiendo un 'rol necesario e importante' en la implementación de planes de seguridad y contingencia, superando la 'capacidad propia'.", "La situación se resolvería más rápido al no esperar apoyo.", "Se fortalecería la autonomía de la guardia."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "El manual menciona la 'Identificación de puntos y áreas vulnerables' como una medida de protección física. Si una Unidad Naval solo identifica los 'Polvorines' como vulnerables, pero ignora las 'Ventanas, escaleras y azoteas colindantes a la calle o edificios contiguos', ¿qué riesgo específico se está dejando desatendido?",
        "opciones": ["El riesgo de incendio exclusivamente.", "El riesgo de 'Ataques armados del tipo Golpe de Mano' o 'Infiltración de personal de la Delincuencia Organizada' a través de puntos de acceso no convencionales y no protegidos.", "El riesgo de accidentes laborales.", "El riesgo de fallas eléctricas."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física / Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "El planeamiento de seguridad debe considerar la 'situación económica y política del área'. Si una Unidad Naval está ubicada en una región con alta actividad de la 'delincuencia organizada' y una economía local inestable que podría generar desempleo, ¿cómo debería este contexto influir en la evaluación de amenazas y vulnerabilidades?",
        "opciones": ["Solo se debe considerar la amenaza directa de la delincuencia organizada.", "El contexto económico y político adverso podría intensificar amenazas como 'Ataques armados del tipo Golpe de Mano' y 'Cooptación de personal', y aumentar vulnerabilidades como la 'Debilidad del sistema de control y confianza institucional', requiriendo un análisis más profundo y medidas preventivas adaptadas.", "No hay relación entre la economía y la seguridad naval.", "Solo se deben considerar los riesgos naturales."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física / Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "El Prefacio menciona que el manual 'norma las caracteristicas, procedimientos, equipo y material empleado para la seguridad de las instalaciones navales'. Si una Unidad adquiere equipo de seguridad de última generación, pero no se adhiere a los 'procedimientos' normados, ¿cuál es la consecuencia esperada para la eficacia de la seguridad?",
        "opciones": ["La seguridad será óptima debido al equipo moderno.", "La eficacia de la seguridad podría verse comprometida, ya que el equipo sin la aplicación correcta de los procedimientos normados no funcionará a su máximo potencial.", "Los procedimientos son menos importantes que el equipo.", "No hay consecuencia, el equipo compensa cualquier deficiencia."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "La 'organización de la Seguridad Física' incluye 'Jefe de Seguridad', 'Supervisores de Seguridad', y 'Servicios de Guardia'. Si hay una falla de comunicación recurrente entre el Jefe de Seguridad y los Supervisores, ¿qué impacto directo podría tener esto en la 'ejecución de acciones para la seguridad física' y la 'acción planeada'?",
        "opciones": ["La comunicación es secundaria, no afectaría la ejecución.", "Podría llevar a una ejecución ineficaz o descoordinada de las acciones de seguridad, ya que los supervisores son los 'ejecutantes de la acción planeada' bajo el mando del Jefe de Seguridad.", "Los supervisores actuarían independientemente y con mayor rapidez.", "Solo afectaría la documentación de los procedimientos."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "El manual indica que los 'Riesgos en las Unidades y Establecimientos Navales son condiciones que pueden dar como resultado la pérdida o daño de recursos humanos, materiales y financieros'. Si se produce un 'Incendio' (considerado un riesgo natural pero también causado por el hombre) debido a 'Ausencia de procedimientos de seguridad contraincendios', ¿cómo se interrelacionan la amenaza, la vulnerabilidad y el riesgo en este escenario?",
        "opciones": ["La amenaza es la inundación, la vulnerabilidad es la falta de personal.", "La amenaza es el incendio, la vulnerabilidad es la 'Ausencia de procedimientos de seguridad contraincendios', y el riesgo materializado es la 'pérdida o daño de recursos humanos, materiales y financieros'.", "El riesgo es la tormenta, la amenaza es el descuido humano.", "No hay interrelación, son eventos aislados."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física / Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "El concepto de 'Protección Física' busca que las unidades y establecimientos 'conserven de manera óptima las capacidades y funciones'. Si las 'Medidas de Protección Física' (como las barreras perimétricas o la iluminación) son inadecuadas, ¿qué efecto directo podría tener esto en la capacidad operativa de una Unidad Naval después de un incidente?",
        "opciones": ["La capacidad operativa se mantendría inalterada.", "La Unidad podría sufrir una 'desorganización' y 'pérdida de la eficiencia y efectividad en el cumplimiento de la misión', al no 'conservar de manera óptima las capacidades y funciones' debido a la ineficacia de las medidas de protección.", "Solo afectaría la apariencia de la instalación.", "La unidad se volvería más flexible."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "Si un 'Oficial de Cuartel' o 'Guardia en Prevención' no cuestiona la presencia de 'desconocidos no escoltados por personal autorizado', ¿qué vulnerabilidad fundamental se expone en el sistema de seguridad?",
        "opciones": ["La 'Falta de controles sanitarios adecuados'.", "La 'Debilidad del sistema de control y confianza institucional' y una 'Deficiencia de la cultura de prevención y seguridad' por parte del personal encargado del 'reconocimiento del personal'.", "La 'Apatía para la supervisión de material clasificado'.", "La 'Omisión al seguimiento de fenómenos hidrometeorológicos'."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física / Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "El manual indica que los 'elementos integrantes de la guardia en prevención' deben tener 'consignas generales y especiales por escrito que incluyan el mayor número de ordenamientos para garantizar la ejecución del servicio de guardia de forma eficiente y efectiva'. Si estas consignas son demasiado complejas o ambiguas, ¿qué impacto directo podría tener esto en la 'eficiencia y efectividad' del servicio?",
        "opciones": ["Aumentaría la eficiencia al requerir más razonamiento.", "La complejidad o ambigüedad podría generar 'confusión' y 'desorganización', impidiendo el 'pleno entendimiento' y, por ende, una ejecución 'eficiente y efectiva' del servicio de guardia.", "No tendría impacto, ya que el personal es altamente capacitado.", "Solo afectaría la velocidad de respuesta."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "Si una Unidad Naval depende exclusivamente de 'sistemas de vigilancia de circuito cerrado' para monitorear áreas críticas sin asignar 'personal de monitoreo' capacitado para 'interpretar el lenguaje corporal que denote amenazas', ¿qué deficiencia clave en la aplicación de la protección física se evidencia?",
        "opciones": ["No hay deficiencia, la tecnología es suficiente por sí misma.", "Se evidencia una deficiencia en la optimización del 'recurso humano', ya que los sistemas de vigilancia son 'medios auxiliares' que requieren personal capacitado para su 'desempeño' efectivo y para interpretar las 'amenazas'.", "La deficiencia en la compra de más cámaras.", "La falta de barreras perimétricas."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "El manual establece que el 'alto mando' ha emitido 'instrucciones y directivas para incrementar las medidas de seguridad'. Si un mando subordinado decide no 'adecuar' estas directivas a las 'características propias de la unidad o establecimiento', ¿qué riesgo se introduce en la aplicación de la protección física?",
        "opciones": ["No se introduce ningún riesgo, la directiva general es suficiente.", "Se introduce el riesgo de que las medidas de protección física sean ineficaces o inaplicables, ya que no consideran los 'factores de riesgo' y 'vulnerabilidades' específicas de la unidad.", "Solo afectaría la burocracia, no la seguridad real.", "La seguridad se volvería más compleja de lo necesario."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "Considerando que la 'Fuga de información' es una amenaza y el 'Descuido en el manejo de información clasificada' es una vulnerabilidad, ¿qué papel juega la 'Certificación de necesidad de acceso a la información' en la mitigación de esta amenaza y vulnerabilidad?",
        "opciones": ["No tiene relación, solo es un requisito administrativo.", "Es un mecanismo de 'control de accesos' que asegura que solo el personal acreditado con una 'necesidad' legítima acceda a la información clasificada, reduciendo el riesgo de fuga por descuido o intención.", "Aumenta el riesgo de fuga al generar más documentos.", "Solo se aplica a información no clasificada."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física / Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "El manual indica que los 'Servicios de Apoyo' son recursos humanos para la seguridad. Si durante un plan de contingencia se activa un 'zafarrancho', pero el personal de 'Servicios de Apoyo' no está familiarizado con su rol, ¿qué impacto tendría en la 'acción conjunta para combatir la amenaza común'?",
        "opciones": ["No tendría impacto, ya que la guardia en prevención es la única crucial.", "Comprometería la 'acción conjunta' y la 'reacción rapida y eficaz', ya que los Servicios de Apoyo 'asumen roles necesarios e importantes' y su desconocimiento impediría el éxito del plan.", "Los servicios de apoyo solo son relevantes para tareas administrativas.", "La familiarización solo es necesaria para el personal de armas."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física / Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "El 'control de paquetes' implica la 'previa inspección y autorización'. Si una Unidad Naval decide omitir esta inspección para agilizar el proceso de recepción, ¿qué riesgos específicos, en el contexto de amenazas antropogénicas, se están introduciendo?",
        "opciones": ["Solo el riesgo de recibir paquetes equivocados.", "Se introduce el riesgo de 'introducción de dispositivos o componentes perjudiciales', o 'robo y/o pérdida de material clasificado' por 'Infiltración de personal de la Delincuencia Organizada' disfrazados de proveedores.", "El riesgo de retrasar la entrega de otros paquetes.", "El riesgo de que los paquetes no sean de la marca deseada."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física / Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "Si una Unidad Naval prioriza el cumplimiento de su misión principal sin dedicar recursos o atención suficiente a la 'seguridad física', ¿qué consecuencia a largo plazo podría tener esto en el 'normal funcionamiento' y la capacidad de la unidad para 'salvaguardar los recursos humanos, materiales y financieros'?",
        "opciones": ["La misión principal se cumpliría más rápidamente.", "Podría generar un deterioro de la seguridad que, eventualmente, comprometería el 'normal funcionamiento' y la capacidad de 'salvaguardar los recursos', llevando a 'desorganización y la pérdida de la eficiencia y efectividad en el cumplimiento de la misión'.", "Se optimizarían los recursos al enfocar solo la misión principal.", "La seguridad es un factor secundario para el funcionamiento."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Introducción / Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "El manual enfatiza la 'revisión y corrección' de las propuestas para mejorar el modelo doctrinario. ¿Qué implicación tiene este proceso de retroalimentación en la naturaleza dinámica de las 'amenazas y vulnerabilidades' que enfrentan las instalaciones navales?",
        "opciones": ["El proceso de retroalimentación es solo burocrático y no afecta la adaptación.", "Permite que el modelo doctrinario se adapte y mejore continuamente para responder a la 'dinámica de las amenazas de los grupos antagónicos' y las cambiantes vulnerabilidades, manteniendo su relevancia y efectividad.", "Las amenazas y vulnerabilidades son estáticas, por lo que la revisión es innecesaria.", "La revisión solo se hace por formalidad, no por necesidad operativa."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Prefacio y Introducción / Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "Si la 'organización de la Seguridad Física' no asigna de forma explícita la figura de 'jefe de seguridad', o si la asigna a personal que no es 'idóneo', ¿qué brecha fundamental se crea en la estructura de responsabilidad de seguridad?",
        "opciones": ["No se crea ninguna brecha, otros miembros pueden asumir el rol.", "Se crea una brecha en la 'responsabilidad' clara de la seguridad y en la 'ejecución de acciones para la seguridad física', comprometiendo el diagnóstico y planeamiento adecuados.", "Solo afectaría la parte administrativa, no la operativa.", "La brecha se compensaría con la experiencia del personal."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "El documento menciona 'Perdida o robo de claves de encriptación o de equipos de comunicación' como una vulnerabilidad. Si un incidente de este tipo ocurre, ¿qué amenaza específica podría materializarse y con qué consecuencia potencial para la institución?",
        "opciones": ["La amenaza de 'incendio', sin mayores consecuencias.", "La amenaza de 'Fuga de información' o 'Intervención de señales de radio y equipos de comunicación', lo que podría 'trastocar las percepciones de seguridad' y comprometer la misión.", "La amenaza de 'Fenómenos hidrometeorológicos'.", "No hay amenaza directa, solo es un inconveniente."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades / Introducción"
    },
    {
        "pregunta": "La 'Identificación de Activos Prioritarios a Proteger' lleva a denominar estas áreas como 'Área Blanca'. Si una Unidad Naval no realiza un estudio de vulnerabilidad adecuado para identificar estos activos, ¿qué impacto podría tener esto en la asignación de medidas de seguridad y la protección de lo más crítico?",
        "opciones": ["Todas las áreas recibirían la misma protección, optimizando recursos.", "Las 'medidas de seguridad' y 'mecanismos extras de refuerzo' podrían no ser asignados a los verdaderos activos prioritarios, dejándolos expuestos a riesgos y vulnerabilidades.", "Solo se protegerían los activos menos importantes.", "La identificación de activos no es crucial para la seguridad."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "El manual indica que los sistemas de comunicaciones deben establecer y mantener 'enlaces de comunicaciones confiables, seguros y rápidos'. Si un plan de comunicaciones es obsoleto o carece de un 'sistema alterno adecuado', ¿qué impacto directo podría tener esto en la capacidad de respuesta del servicio de guardia ante una emergencia?",
        "opciones": ["La respuesta sería más lenta y menos coordinada, ya que la 'intercomunicación eficiente y efectiva' se vería comprometida, afectando la 'reacción rapida y eficaz'.", "No tendría impacto, ya que el personal se comunicaría verbalmente.", "Mejoraría la comunicación al no tener alternativas.", "Solo afectaría la comunicación con unidades externas."],
        "respuesta_correcta": 0,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física"
    },
    {
        "pregunta": "Si un programa de seguridad física carece de una 'evaluación del programa, los instructores y el personal naval participante para una retroalimentación que permita mejorar los programas de forma permanente y continua', ¿qué consecuencia a largo plazo podría tener esto en la eficacia general del programa?",
        "opciones": ["El programa se mantendría estático, sin adaptarse a nuevas amenazas o fallas en su implementación, lo que llevaría a una disminución gradual de su eficacia y a una 'deficiencia de la cultura de prevención y seguridad'.", "El programa sería perfecto desde el inicio y no necesitaría mejoras.", "La eficacia aumentaría al no perder tiempo en evaluaciones.", "Solo afectaría la calidad de los instructores, no del programa."],
        "respuesta_correcta": 0,
        "dificultad": "dios",
        "tema": "Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "El documento fue una 'actualización del DAM 1.3.3.5.7'. ¿Qué demuestra este hecho sobre la naturaleza de la doctrina de seguridad en la Secretaría de Marina Armada de México?",
        "opciones": ["La doctrina de seguridad es estática y no cambia.", "La doctrina de seguridad es dinámica y evolutiva, adaptándose a nuevas experiencias y contextos para mantener su relevancia y efectividad.", "La doctrina de seguridad es un documento obsoleto.", "La doctrina de seguridad es solo un requisito administrativo."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Prefacio y Introducción"
    },
    {
        "pregunta": "Los 'factores que afectan la seguridad física' incluyen 'capacidades propias y del enemigo'. Si el planeamiento de seguridad no evalúa adecuadamente las 'capacidades del enemigo o trasgresor de la ley', ¿qué tipo de riesgo se materializa para la Unidad Naval?",
        "opciones": ["El riesgo de sobreestimar las amenazas.", "El riesgo de subestimar las amenazas y vulnerabilidades, llevando a una planificación insuficiente y a una exposición a 'ataques directos' o 'actos intencionales' que superen las 'capacidades propias'.", "El riesgo de invertir en seguridad innecesariamente.", "El riesgo de que el personal se aburra."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "El manual menciona la 'Organización de la Seguridad Física' con la figura del 'Jefe de Seguridad' y 'Supervisores de Seguridad'. ¿Qué implicación tiene la ausencia de una estructura de mando clara o la falta de nombramientos formales para estos roles en la respuesta coordinada ante una amenaza?",
        "opciones": ["No habría implicación, ya que el personal actuaría por iniciativa.", "La ausencia de una estructura de mando clara podría generar 'desorganización' y confusión, impidiendo una 'reacción rapida y eficaz' y la 'preservación de los recursos'.", "Se fomentaría la autonomía del personal.", "Solo afectaría las tareas rutinarias, no las emergencias."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física"
    },
    {
        "pregunta": "Si una Unidad Naval no realiza 'revisiones aleatorias a las taquillas y maletas del personal naval', ¿qué vulnerabilidad se mantiene activa y qué amenazas específicas podría facilitar su omisión?",
        "opciones": ["No se mantiene ninguna vulnerabilidad activa.", "Se mantiene activa la vulnerabilidad de 'falta de controles' y 'debilidad del sistema de control y confianza institucional', lo que podría facilitar amenazas como 'robo hormiga de productos diversos' o 'venta de estupefacientes al interior de las instalaciones navales'.", "Solo facilita la comodidad del personal.", "Facilita la entrada de alimentos."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "El Prefacio indica que el conocimiento adquirido por el personal naval es de 'gran valor'. Si la capacitación en el modelo doctrinario es deficiente o incompleta, ¿qué consecuencia a largo plazo podría tener esto en la capacidad del personal para aplicar las medidas de seguridad y prevenir incidentes?",
        "opciones": ["El personal aprendería por sí mismo a través de la experiencia.", "La deficiencia en el conocimiento podría llevar a una 'deficiencia de la cultura de prevención y seguridad' y a la incapacidad de aplicar correctamente las 'características, procedimientos, equipo y material' de seguridad, aumentando la 'vulnerabilidad' a incidentes.", "La capacitación es un gasto innecesario si ya tienen experiencia.", "Solo afectaría a los nuevos ingresos, no al personal experimentado."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Prefacio y Introducción / Capítulo IV. Cultura de Seguridad Física"
    },
    {
        "pregunta": "El concepto de 'riesgo' se define como la 'probabilidad de que se produzca un evento y sus consecuencias negativas'. Si una Unidad Naval solo se enfoca en las 'consecuencias negativas' de un evento pasado sin analizar la 'probabilidad' de eventos futuros (por ejemplo, después de un desastre natural), ¿qué deficiencia en la gestión del riesgo se presenta?",
        "opciones": ["No hay deficiencia, ya que las consecuencias son lo más importante.", "La deficiencia en la capacidad de 'prevenir' o mitigar la recurrencia de eventos, ya que no se evalúa la probabilidad de las 'amenazas y vulnerabilidades' futuras que podrían llevar a nuevas 'pérdidas o daños'.", "La deficiencia de recursos financieros.", "La deficiencia de personal."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo I. Seguridad Física / Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "La introducción menciona que la 'seguridad física... ha cobrado mayor relevancia a raíz de los hechos suscitados en el estado de Chiapas el 1 de enero de 1994' y la participación contra la delincuencia organizada. ¿Qué demuestra esto sobre la influencia de los eventos históricos y el contexto sociopolítico en la evolución de las políticas de seguridad naval?",
        "opciones": ["Los eventos históricos no tienen influencia en las políticas de seguridad.", "Demuestra que los eventos históricos y el contexto sociopolítico son catalizadores para la 'actualización de las capacidades' y el desarrollo de 'instrucciones y directivas' que refuerzan la seguridad física, respondiendo a amenazas emergentes.", "La seguridad naval se mantiene aislada de los eventos externos.", "Los eventos históricos solo afectan el pasado, no el presente de la seguridad."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Introducción"
    },
    {
        "pregunta": "Si una unidad o establecimiento naval tiene un 'Área Negra' con el 'mínimo de control' y es el 'área más vulnerable', pero el personal de guardia no tiene la instrucción de cuestionar la presencia de desconocidos en estas áreas, ¿qué riesgo inminente se presenta para la seguridad general de la instalación?",
        "opciones": ["El riesgo de que el personal se sienta demasiado cómodo.", "Se presenta el riesgo de 'Infiltración de personal de la Delincuencia Organizada' o la realización de 'Actos intencionales de comisión u omisión' en la zona más susceptible, comprometiendo la seguridad de toda la instalación.", "El riesgo de sobrecarga de trabajo para el personal.", "El riesgo de que las personas se pierdan en el área."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Capítulo III. Protección Física / Capítulo II. Amenazas y Vulnerabilidades"
    },
    {
        "pregunta": "El manual busca 'orientar y normar la actuación del personal'. Si la Secretaría de Marina Armada de México no logra 'generar planes de contingencias que garanticen la seguridad' frente a los riesgos y vulnerabilidades identificados, ¿cuál sería la consecuencia final para la 'Misión' de la institución de 'emplear el Poder Naval de la Federación para la defensa exterior y coadyuvar en la seguridad interior del país'?",
        "opciones": ["La Misión se fortalecería al enfocarse en el poder naval únicamente.", "La Misión de la institución se vería fundamentalmente comprometida, ya que la incapacidad de salvaguardar sus recursos y responder a amenazas socavaría su 'eficiencia y efectividad en el cumplimiento de la misión' y su capacidad para 'coadyuvar en la seguridad interior del país'.", "La Misión cambiaría para adaptarse a la falta de seguridad.", "La Misión solo se vería afectada en tiempos de paz."],
        "respuesta_correcta": 1,
        "dificultad": "dios",
        "tema": "Introducción / Capítulo III. Protección Física"
    },
]