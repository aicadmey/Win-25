class Human:
  def __init__(self, name, age, gender):
    self.name= name
    self.age= age
    self.gender= gender

  def display_info(self):
    print(f"Name: {self.name} ")
    print(f"Age: {self.age} ")
    print(f"Gender: {self.gender} ")


class Bone(Human):
      def __init__(self, name, age, gender, bone_name, bone_location):
        super().__init__(name, age, gender)
        self.bone_name= name
        self.bone_location= bone_location

      def display_info(self):
        super().display_info()
        print(f"Bone Name: {self.bone_name} ")
        print(f"Bone Location: {self.bone_location} ")

      def bone_function(self):
        print(f"{self.bone_name} is Helps in Structural Support. ")

class Skull(Bone):
  def __init__(self, name, age, gender, bone_name, bone_location, protection_area):
    super().__init__(name, age, gender, bone_name, bone_location)
    self.protection_area= protection_area

  def bone_function(self):
    print(f"{self.bone_name} is Protecting the {self.protection_area} ")

class Femur(Bone):
  def __init__(self,name, age, gender, bone_name, bone_location, support_area):
    super().__init__(name, age, gender, bone_name, bone_location)
    self.support_area= support_area

  def bone_function(self):
    print(f"{self.bone_name} Support Body Weight with Strength Level {self.support_area} ")

skull= Skull("Usman", 22, "Male", "Skull", "Head Topmost Part", "Brain" )
femur= Femur("Usman", 22, "Male", "Femur", "Thigh Bone", "High" )

print("Skull Information ")
skull.display_info()
skull.bone_function()

print("\n Femur Information ")
femur.display_info()
femur.bone_function()

class Muscles(Human):
   def __init__(self, name, age, gender, muscles_name, muscles_location):
    super().__init__(name, age, gender)
    self.muscles_name= muscles_name
    self.muscles_location= muscles_location

   def display_info(self):
    super().display_info()
    print(f"Muscles Name: {self.muscles_name} ")
    print(f"Muscles Location: {self.muscles_location} ")

   def muscles_function(self):
    print(f"{self.muscles_name} is Enable Movement in Human Body. ")

class Skeletal_Muscle(Muscles):
  def __init__(self, name, age, gender, muscles_name, muscles_location, skeletal_strength):
    super().__init__(name, age, gender, muscles_name, muscles_location)
    self.skeletal_strength= skeletal_strength

  def muscles_function(self):
    print(f"{self.muscles_name} is Strengthen the {self.skeletal_strength} ")


class Biceps(Skeletal_Muscle):
  def __init__(self, name, age, gender, muscles_name, muscles_location, skeletal_strength, size):
    super().__init__(name, age, gender, muscles_name, muscles_location, skeletal_strength)
    self.size= size

  def muscles_function(self):
    print(f"{self.muscles_name} Helps in Arms Movement. Size: {self.size} ")

class Triceps(Skeletal_Muscle):
  def __init__(self, name, age, gender, muscles_name, muscles_location, skeletal_strength, size):
    super().__init__(name, age, gender, muscles_name, muscles_location, skeletal_strength)
    self.size= size

  def muscles_function(self):
    print(f"{self.muscles_name} Extends the Elbow and Straighten the Arm. Size: {self.size} ")

class Forearm(Skeletal_Muscle):
  def __init__(self, name, age, gender, muscles_name, muscles_location, skeletal_strength, size):
    super().__init__(name, age, gender, muscles_name, muscles_location, skeletal_strength)
    self.size= size

  def muscles_function(self):
    print(f"{self.muscles_name} Extends the knee, enabling walking, running, and jumping. Size: {self.size} ")

bicep= Biceps("Usman", 22, "Male", "Biceps", "Arm", "Movement of Arms ", "Small")
tricep= Triceps("Usman", 22, "Male", "Triceps", "Arm", "Movement of Arms ", "Medium")
forearm= Forearm("Usman", 22, "Male", "Forearm", "Arm", "Movement of Arms ", "Large")

print("Biceps Information in Skeletal Muscle ")
bicep.display_info()
bicep.muscles_function()

print("\n Triceps Information in Skeletal Muscle ")
tricep.display_info()
tricep.muscles_function()

print("\n Forearm Information in Skeletal Muscle ")
forearm.display_info()
forearm.muscles_function()


class Cardiac_Muscle(Muscles):
  def __init__(self, name, age, gender, muscles_name, muscles_location, cardiac_strength):
    super().__init__(name, age, gender, muscles_name, muscles_location)
    self.cardiac_strength= cardiac_strength

  def muscles_function(self):
    print(f"{self.muscles_name} is Strengthen the {self.cardiac_strength} ")

class Atria(Cardiac_Muscle):
  def __init__(self, name, age, gender, muscles_name, muscles_location, cardiac_strength, size):
    super().__init__(name, age, gender, muscles_name, muscles_location, cardiac_strength)
    self.size= size

  def muscles_function(self):
    print(f"{self.muscles_name} Receive blood returning to the heart. Size: {self.size} ")

class Ventricles(Cardiac_Muscle):
    def __init__(self, name, age, gender, muscles_name, muscles_location, cardiac_strength, pump_rate):
        super().__init__(name, age, gender, muscles_name, muscles_location, cardiac_strength)
        self.pump_rate = pump_rate

    def muscles_function(self):
        print(f"{self.muscles_name} pumps blood out of the heart. Pump Rate: {self.pump_rate} bpm")

class Septum(Cardiac_Muscle):
  def __init__(self, name, age, gender, muscles_name, muscles_location, septum_strength, size):
    super().__init__(name, age, gender, muscles_name, muscles_location, septum_strength)
    self.size= size

  def muscles_function(self):
    print(f"{self.muscles_name} Separates the left and right sides of the heart, preventing mixing of oxygenated and deoxygenated blood. Size: {self.size} ")

atria= Atria("Usman", 22, "Male", "Atria", "Heart", "Movement of Heart ", "Large")
ventricles= Ventricles("Usman", 22, "Male", "Ventricles", "Heart", "Movement of Heart ", "Small")
septum= Septum("Usman", 22, "Male", "Septum", "Heart", "Movement of Heart ", "Medium")

print("Atria Information in Cardiac Muscles ")
atria.display_info()
atria.muscles_function()

print("\n Ventricles Information in Cardiac Muscles ")
ventricles.display_info()
ventricles.muscles_function()

print("\n Septum Information in Cardiac Muscles ")
septum.display_info()
septum.muscles_function()

class Smooth_Muscle(Muscles):
  def __init__(self, name, age, gender, muscles_name, muscles_location, smooth_strength):
    super().__init__(name, age, gender, muscles_name, muscles_location)
    self.smooth_strength= smooth_strength

  def muscles_function(self):
    print(f"{self.muscles_name} is Strengthen {self.smooth_strength} ")

class Intestinal(Smooth_Muscle):
  def __init__(self, name, age, gender,muscles_name, muscles_location, smooth_strength, digestion_rate):
    super().__init__(name, age, gender, muscles_name, muscles_location, smooth_strength)
    self.digestion_rate= digestion_rate

  def muscles_function(self):
    print(f"{self.muscles_name} Helps in Digestive System. Digestion Rate: {self.digestion_rate} ")

class Bladder(Smooth_Muscle):
  def __init__(self, name, age, gender, muscles_name, muscles_location, smooth_strength, control_level):
    super().__init__(name, age, gender, muscles_name, muscles_location, smooth_strength)
    self.control_level= control_level

  def muscles_function(self):
    print(f"{self.muscles_name} Store Urine Until it is Excreted from the Body. Control Level: {self.control_level} ")

class Esophagus(Smooth_Muscle):
  def __init__(self, name, age, gender, muscles_name, muscles_location, smooth_strength, contraction_speed):
    super().__init__(name, age, gender, muscles_name, muscles_location, smooth_strength)
    self.contraction_speed= contraction_speed

intestinal= Intestinal("Usman", 22, "Male", "Intestinal", "Abdomen", "Small Intestine", "6-8 Hours ")
bladder= Bladder("Usman", 22, "Male", "Bladder", "Pelvic Cavity", "Small Intestine", "1-2 Days ")
esophagus= Esophagus("Usman", 22, "Male", "Esophagus", "Chest", "Small Intestine", "2-4 Centimeters per Second ")

print("Intestinal Information in Smooth Muscles")
intestinal.display_info()
intestinal.muscles_function()

print("\n Bladder Information in Smooth Muscles")
bladder.display_info()
bladder.muscles_function()

print("\n Esophagus Information in Smooth Muscles")
esophagus.display_info()
esophagus.muscles_function()

skeletal= Skeletal_Muscle("Usman", 22, "Male", "Biceps", "Arm", "Movement of Arms ")
cardiac= Cardiac_Muscle("Usman", 22, "Male", "Triceps", "Arm", "Movement of Arms ")
smooth= Smooth_Muscle("Usman", 22, "Male", "Forearm", "Arm", "Movement of Arms ")

print("Skeletal Muscle Information ")
skeletal.display_info()
skeletal.muscles_function()

print("\n Cardiac Muscle Information ")
cardiac.display_info()
cardiac.muscles_function()

print("\n Smooth Muscle Information ")
smooth.display_info()
smooth.muscles_function()


class Neurons(Human):
  def __init__(self, name, age, gender, neurons_name, neurons_location):
    super().__init__(name, age, gender)
    self.neurons_name= neurons_name
    self.neurons_location= neurons_location

  def display_info(self):
    print(f"Neurons Name: {self.neurons_name} ")
    print(f"Neurons Location: {self.neurons_location} ")

  def neurons_function(self):
    print(f"{self.neurons_name} Transmits Electrical and Chemical Signals Throughout The Body. ")

class Sensory_Neurons(Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, sensory_strength):
    super().__init__(name, age, gender, neurons_name, neurons_location)
    self.sensory_strength= sensory_strength

  def neurons_function(self):
    print(f"{self.neurons_name} Stimulate the {self.sensory_strength} ")

class Hearing_Neurons(Sensory_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, sensory_strength, frequency_rate):
    super().__init__(name, age, gender, neurons_name, neurons_location, sensory_strength)
    self.frequency_rate= frequency_rate

  def neurons_function(self):
    print(f"{self.neurons_name} Stimulate the Hearing. Frequency: {self.frequency_rate} ")

class Vision_Neurons(Sensory_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, sensory_strength, signal_strength):
    super().__init__(name, age, gender, neurons_name, neurons_location, sensory_strength)
    self.signal_strength= signal_strength

  def neurons_function(self):
    print(f"{self.neurons_name} Transmits The Signals. Signal: {self.signal_strength} ")

class Touch_Neurons(Sensory_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, sensory_strength, sensitivity_level):
    super().__init__(name, age, gender,neurons_name, neurons_location, sensory_strength)
    self.sensitivity_level= sensitivity_level

  def neurons_function(self):
    print(f"{self.neurons_name} Stimulate the Touch. Sensitivity: {self.sensitivity_level} ")

class Smell_Neurons(Sensory_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, sensory_strength, odor_recogination):
    super().__init__(name, age, gender, neurons_name, neurons_location, sensory_strength)
    self.odor_recogination= odor_recogination
          
  def neurons_function(self):
    print(f"{self.neurons_name} Stimulate thr Smell Odor. Recogination: {self.odor_recogination} ")

hearing= Hearing_Neurons("Usman", 22, "Male", "Ear", "Head", "Auditory", "20Hz to 20KHz")
vision= Vision_Neurons("Usman", 22, "Male", "Eye", "Head", "Visual", "Factors By Factors" )
touch= Touch_Neurons("Usman", 22, "Male", "Finger", "Hand", "Tactile", "High" )
smell= Smell_Neurons("Usman", 22, "Male", "Nose", "Head", "Smell", "High" )

print("Hearing Information in Sensory Neurons ")
hearing.display_info()
hearing.neurons_function()

print("\n Vision Information in Sensory Neurons")
vision.display_info()
vision.neurons_function()

print("\n Touch Information in Sensory Neurons ")
touch.display_info()
touch.neurons_function()


print("\n Smell Information in Sensory Neurons ")
smell.display_info()
smell.neurons_function()

class Motor_Neurons(Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, motor_area):
    super().__init__(name, age, gender, neurons_name, neurons_location)
    self.motor_area= motor_area

  def neurons_function(self):
    print(f"{self.neurons_name} in {self.motor_area} Controls The Motor Activities. ")

class Skeletal_Motor(Motor_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, motor_area, skeletal_strength):
    super().__init__(name, age, gender, neurons_name, neurons_location, motor_area)
    self.skeletal_strength= skeletal_strength
          
  def neurons_function(self):
    print(f"{self.neurons_name} Transmits Signals from Central Nervous System to Skeletal Muscles. Skeletal Strength: {self.skeletal_strength} ")

class Facial_Motor(Motor_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, motor_area, expression_type):
    super().__init__(name, age, gender, neurons_name, neurons_location, motor_area)
    self.expression_type= expression_type
          
  def neurons_function(self):
    print(f"{self.neurons_name} Controls the Musces Responsible for Facial Expressions. Expression Type: {self.expression_type} ")

class Limb_Motor(Motor_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, motor_area, coordination_level):
    super().__init__(name, age, gender, neurons_name, neurons_location, motor_area)
    self.coordination_level= coordination_level
          
  def neurons_function(self):
    print(f"{self.neurons_name} Transmits Motor Signals From Brain to Muscles. Coordination Level: {self.coordination_level} ")

class Speech_Motor(Motor_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, motor_area, fluency_level):
    super().__init__(name, age, gender, neurons_name, neurons_location, motor_area)
    self.fluency_level= fluency_level
          
  def neurons_function(self):
    print(f"{self.neurons_name} Controls the Coordination of Muscles Movements. Fluency Level: {self.fluency_level} ")

skeletal= Skeletal_Motor("Usman", 22, "Male", "Somatic Motor Neurons", "Spinal Cord", "Motor Cortex", "Motor Strength")
facial= Facial_Motor("Usman", 22, "Male", "Facial Motor Neurons", "Face", "Somatotopy", "Facial Expression")
limb= Limb_Motor("Usman", 22, "Male", "Limbic", "Motor Cortex", "Premotor Cortex", "Coordination Level")
speech= Speech_Motor("Usman", 22, "Male", "Auditory Motor Neurons", "Spinal Cord", "Motor Cortex", "Fluency Level")

          
print("Skeletal Motor Information in Motor Neurons")
skeletal.display_info()
skeletal.neurons_function()

print("\n Facial Motor Information in Motor Neurons")
facial.display_info()
facial.neurons_function()

print("\n Limb Motor Information in Motor Neurons")
limb.display_info()
limb.neurons_function()

print("\n Speech Motor Information in Motor Neurons")
speech.display_info()
speech.neurons_function()

          
class Interneurons(Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, interneurons_type):
    super().__init__(name, age, gender, neurons_name, neurons_location)
    self.interneurons_type= interneurons_type
          
  def neurons_function(self):
    print(f"{self.neurons_name} Connect Sensory and Motor Neurons With CNS. Neurons Type: {self.interneurons_type}")

class Local_Interneurons(Interneurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, interneurons_type, reflex_action):
    super().__init__(name, age, gender, neurons_name, neurons_location, interneurons_type)
    self.reflex_action= reflex_action
          
  def neurons_function(self):
    print(f"{self.neurons_name} Reflex neurons enable quick, involuntary reactions by transmitting signals through the spinal cord, bypassing the brain. Reflex Action{self.reflex_action}" )

class Projection_Interneurons(Interneurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, interneurons_type, projection_area):
    super().__init__(name, age, gender, neurons_name, neurons_location, interneurons_type)
    self.projection_area= projection_area
          
  def neurons_function(self):
    print(f"{self.neurons_name} Projection interneurons transmit signals between distant regions of the CNS. Projection Area: {self.projection_area} ")

class Inhibitory_Interneurons(Interneurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, interneurons_type, inhibitory_strength):
    super().__init__(name, age, gender, neurons_name, neurons_location, interneurons_type)
    self.inhibitory_strength= inhibitory_strength
          
  def neurons_function(self):
    print(f"{self.neurons_name} Modulate neural activity by inhibiting the firing of other neurons, maintaining balance in neural circuits. Inhibitory Strength: {self.inhibitory_strength} ")

class Excitatory_Interneurons(Interneurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, interneurons_type, excitatory_strength):
    super().__init__(name, age, gender, neurons_name, neurons_location, interneurons_type)
    self.excitatory_strength= excitatory_strength
          
  def neurons_function(self):
    print(f"{self.neurons_name} Enhance neural activity by increasing the likelihood of other neurons firing. Excitatory Strength: {self.excitatory_strength}")

local= Local_Interneurons("Usman", 22, "Male", "Short Axon", "Spinal Cord", "Intercalated", "Spinal")
projection= Projection_Interneurons("Usman", 22, "Male", "Long Axon", "Spinal Cord", "Intercalated", "Projection Field")
inhibitory= Inhibitory_Interneurons("Usman", 22, "Male", "Short Axon", "Spinal Cord", "Intercalated", "Inhibitory")
excitatory= Excitatory_Interneurons("Usman", 22, "Male", "Long Axon", "Spinal Cord", "Intercalated", "Excitatory")

print("Local Interneurons Information ")
local.display_info()
local.neurons_function()

print("\n Projection Interneurons Information ")
projection.display_info()
projection.neurons_function()

print("\n Inhibitory Interneurons Information ")
projection.display_info()
projection.neurons_function()

print("\n Excitatory Interneurons Information ")
excitatory.display_info()
excitatory.neurons_function()

          
class Autonomic_Neurons(Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, autonomic_area):
    super().__init__(name, age, gender, neurons_name, neurons_location)
    self.autonomic_area= autonomic_area
          
  def neurons_function(self):
    print(f"{self.neurons_name} Which Controls Involuntary Bodily Functions. Auntonomic Area: {self.autonomic_area}")

class Sympathetic_Neurons(Autonomic_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, autonomic_area, connection_type):
    super().__init__(name, age, gender, neurons_name, neurons_location, autonomic_area)
    self.connection_type= connection_type
          
  def neurons_function(self):
    print(f"{self.neurons_name} Trigger the fight or flight response, increasing heart rate, dilating airways, and mobilizing energy. Connection Type: {self.connection_type}")

class Parasympathetic_Neurons(Autonomic_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, autonomic_area, connection_type):
    super().__init__(name, age, gender, neurons_name, neurons_location, autonomic_area)
    self.connection_type= connection_type
          
  def neurons_function(self):
    print(f"{self.neurons_name} Promote the rest and digest response, slowing heart rate, stimulating digestion, and conserving energy. Connection Type: {self.connection_type}")

class Preganglionic_Neurons(Autonomic_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, autonomic_area, connection_type):
    super().__init__(name, age, gender, neurons_name, neurons_location, autonomic_area)
    self.connection_type= connection_type
          
  def neurons_function(self):
    print(f"{self.neurons_name} Transmit signals from the central nervous system to autonomic ganglia (clusters of neurons). Connection Type: {self.connection_type}")

class Postganglionic_Neurons(Autonomic_Neurons):
  def __init__(self, name, age, gender, neurons_name, neurons_location, autonomic_area, connection_type):
    super().__init__(name, age, gender, neurons_name, neurons_location, autonomic_area)
    self.connection_type= connection_type
          
  def neurons_function(self):
    print(f"{self.neurons_name} Relay signals from autonomic ganglia to target organs like the heart, lungs, or intestines. Connection Type: {self.connection_type}")

sympathetic= Sympathetic_Neurons("Usman", 22, "Male", "Sympathetic", "Spinal", "Thoracolumber", "Autonomic")
parasympathetic= Parasympathetic_Neurons("Usman", 22, "Male", "Parasympathetic", "Spinal", "Vagus", "Autonomic")
preganglionic= Preganglionic_Neurons("Usman", 22, "Male", "Preganglionic", "Spinal", "Sympathetic", "Autonomic")
postganglionic= Postganglionic_Neurons("Usman", 22, "Male", "Postganglionic", "Spinal", "Autonomic Ganglia", "Autonomic")

print("Sympathetic Neurons Information")
sympathetic.display_info()
sympathetic.neurons_function()

print("\n Parasympathetic Neurons Information")
parasympathetic.display_info()
parasympathetic.neurons_function()

print("\n Preganglionic Neurons Information")
preganglionic.display_info()
preganglionic.neurons_function()

print("\n Postganglionic Neurons Information")
postganglionic.display_info()
postganglionic.neurons_function()

          

sensory= Sensory_Neurons("Usman", 22, "Male", "Ear", "Head", "Auditory")
motor= Motor_Neurons("Usman", 22, "Male", "Somatic Motor Neurons", "Spinal Cord", "Motor Cortex")
interneurons= Interneurons("Usman", 22, "Male", "Short Axon", "Spinal Cord", "Intercalated")
autonomic= Autonomic_Neurons("Usman", 22, "Male", "Sympathetic", "Spinal", "Thoracolumber")

          
print("Sensory Neurons Information")
sensory.display_info()
sensory.neurons_function()

print("\n Motor Neurons Information")
motor.display_info()
motor.neurons_function()

print("\n Interneurons Information")
interneurons.display_info()
interneurons.neurons_function()

print("\n Autonomic Neurons Information")
autonomic.display_info()
autonomic.neurons_function



class Blood(Human):
  def __init__(self, name, age, gender, blood_name, blood_location, red_size):
    super().__init__(name, age, gender)
    self.blood_name= blood_name
    self.blood_location= blood_location
    self.red_size= red_size
  
  def display_info(self):
    print(f"Blood Name: {self.blood_name} ")
    print(f"Blood Location: {self.blood_location} ")

  def blood_function(self):
    print(f"{self.blood_name} Transmits Blood to the Body. ")

class Red_Blood_Cells(Blood):
  def __init__(self, name, age, gender, blood_name, blood_location, red_size):
    super().__init__(name, age, gender, blood_name, blood_location, red_size)
    self.red_size= red_size

  def blood_function(self):
    print(f"{self.blood_name} Stimulate the {self.red_size} ")

class Normocytes(Red_Blood_Cells):
  def __init__(self, name, age, gender, blood_name, blood_location, red_size):
      super().__init__(name, age, gender, blood_name, blood_location, red_size)

  def blood_function(self):
    print(f"{self.blood_name} Efficient oxygen transport using hemoglobin.Size: {self.red_size} ")

class Microcytes(Red_Blood_Cells):
  def __init__(self, name, age, gender, blood_name, blood_location, red_size):
    super().__init__(name, age, gender, blood_name, blood_location, red_size)
    self.red_size = red_size

  def blood_function(self):
    print(f"{self.blood_name} Iron-deficiency anemia or thalassemia. Size: {self.red_size} ")

class Macrocytes(Red_Blood_Cells):
  def __init__(self, name, age, gender, blood_name, blood_location, macroccyte_size, red_size):
    super().__init__(name, age, gender, blood_name, blood_location, red_size)
    self.macroccyte_size= macroccyte_size

  def blood_function(self):
    print(f"{self.blood_name} Vitamin B12 or folic acid deficiency (megaloblastic anemia). Size: {self.red_size} ")

class Sickle_Cells(Red_Blood_Cells):
  def __init__(self, name, age, gender, blood_name, blood_location, sickle_size, red_size):
    super().__init__(name, age, gender, blood_name, blood_location, red_size)
    self.sickle_size= sickle_size

  def blood_function(self):
    print(f"{self.blood_name} anemia, reducing oxygen transport efficiency. Size: {self.red_size} ")

class Codocytes(Red_Blood_Cells):
  def __init__(self, name, age, gender, blood_name, blood_location, codocyte_size, red_size):
    super().__init__(name, age, gender, blood_name, blood_location, red_size)
    self.codocyte_size= codocyte_size
  def blood_function(self):
    print(f"{self.blood_name} Liver disease, thalassemia, or iron-deficiency anemia. Size: {self.red_size} ")

normocytes= Normocytes("Usman", 22, "Male", "Red Blood Cells", "Bone Marrow", "6-8 Micrometers")
microcytes= Microcytes("Usman", 22, "Male", "Red Blood Cells", "Tissus", "6 Omega Meters")
macrocytes= Macrocytes("Usman", 22, "Male", "Red Blood Cells", "Tissus", "6 Omega Meters", "6-8 Micrometers")
sickle_cells= Sickle_Cells("Usman", 22, "Male", "Red Blood Cells", "Blood", "Sickle Cells", "Abnormal")
codocyt= Codocytes("Usman", 22, "Male", "Red Blood Cells", "Blood", "Bullseye", "Normal")

print("Normocytes Information in Red Blood Cells")
normocytes.display_info()
normocytes.blood_function()

print("\n Microcytes Information in Red Blood Cells")
microcytes.display_info()
microcytes.blood_function()

print("\n Macrocytes Information in Red Blood Cells")
macrocytes.display_info()
macrocytes.blood_function()

print("\n Sickle Cells Information in Red Blood Cells")
sickle_cells.display_info()
sickle_cells.blood_function()

print("\n Codocytes Information in Red Blood Cells")
codocyt.display_info()
codocyt.blood_function()

class White_Blood_Cells(Blood):
  def __init__(self, name, age, gender, blood_name, blood_location, white_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.white_strength= white_strength

    def blood_function(self):
     print(f"{self.blood_name} Stimulate the {self.white_strength}")

class Neutrophils(White_Blood_Cells):
  def __init__(self, name, age, gender, blood_name, blood_location, neutrophil_percentage):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.neutrophil_percentage= neutrophil_percentage
          
  def blood_function(self):
    print(f"{self.blood_name} Act as the first line of defense by engulfing and destroying bacteria and fungi. Percentage: {self.neutrophil_percentage} ")

class Lymphocytes(White_Blood_Cells):
  def __init__(self, name, age, gender, blood_name, blood_location, lymphocyte_percentage):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.lymphocyte_percentage= lymphocyte_percentage
          
  def blood_function(self):
    print(f"{self.blood_name} Play a key role in immunity; B-cells produce antibodies, T-cells attack infected cells, and NK cells destroy abnormal cells. Percentage: {self.lymphocyte_percentage} ")

class Monocytes(White_Blood_Cells):
  def __init__(self, name, age, gender, blood_name, blood_location, monocyte_percentage):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.monocyte_percentage= monocyte_percentage
          
  def blood_function(self):
    print(f"{self.blood_name} Differentiate into macrophages to engulf pathogens and debris, and present antigens to lymphocytes. Percentage: {self.monocyte_percentage} ")

class Eosinophils(White_Blood_Cells):
  def __init__(self, name, age, gender, blood_name, blood_location, eosinophil_percentage):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.eosinophil_percentage= eosinophil_percentage
          
  def blood_function(self):
    print(f"{self.blood_name} Fight parasitic infections and play a role in allergic reactions. Percentage: {self.eosinophil_percentage} ")

class Basophils(White_Blood_Cells):
  def __init__(self, name, age, gender, blood_name, blood_location, basophil_percentage):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.basophil_percentage= basophil_percentage
          
  def blood_function(self):
    print(f"{self.blood_name} Release histamine and other chemicals during allergic and inflammatory responses. Percentage: {self.basophil_percentage} ")

neutrophils= Neutrophils("Usman", 22, "Male", "White Blood Cells", "Blood", "50%-70%")
lymphocytes= Lymphocytes("Usman", 22, "Male", "White Blood Cells", "Lymphoid", "20%-40%")
monocytes= Monocytes("Usman", 22, "Male", "White Blood Cells", "Blood", "2-8%")
eosinophils= Eosinophils("Usman", 22, "Male", "White Blood Cells", "Blood", "1-4%")
basophils= Basophils("Usman", 22, "Male", "White Blood Cells", "Blood", "Less Than 1%")

print("Neutrophils Information in White Blood Cells")
neutrophils.display_info()
neutrophils.blood_function()

print("\n Lymphocytes Information in White Blood Cells")
lymphocytes.display_info()
lymphocytes.blood_function()

print("\n Monocytes Information in White Blood Cells")
monocytes.display_info()
monocytes.blood_function()

print("\n Eosinophils Information in White Blood Cells")
eosinophils.display_info()
eosinophils.blood_function()

print("\n Basophils Information in White Blood Cells")
basophils.display_info()
basophils.blood_function()

          
class Platelets(Blood):
  def __init__(self, name, age, gender, blood_name, blood_location, platelet_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.platelet_strength= platelet_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Stimulate the {self.platelet_strength} ")

class Resting_Platelets(Platelets):
  def __init__(self, name, age, gender, blood_name, blood_location, platelet_strength, resting_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.resting_strength= resting_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Inactive platelets circulating in the bloodstream, disc-shaped and ready to respond to vascular injury. Strength: {self.resting_strength} ")

class Active_Platelets(Platelets):
  def __init__(self, name, age, gender, blood_name, blood_location, platelet_strength, active_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.active_strength= active_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Platelets that change shape (becoming spiky) and release granules to promote clotting and recruit more platelets to the injury site. Strength: {self.active_strength} ")

class Large_Platelets(Platelets):
  def __init__(self, name, age, gender, blood_name, blood_location, platelet_strength, large_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.large_strength= large_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Abnormally large platelets often seen in conditions like immune thrombocytopenia or certain genetic disorders. Strength: {self.large_strength} ")

class Hyperactive_Platelets(Platelets):
  def __init__(self, name, age, gender, blood_name, blood_location, platelet_strength, hyperactive_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.hyperactive_strength= hyperactive_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Platelets with increased responsiveness, often associated with conditions like diabetes, atherosclerosis, or cardiovascular diseases. Strength: {self.hyperactive_strength} ")

          
class Hypoactive_Platelets(Platelets):
  def __init__(self, name, age, gender, blood_name, blood_location, platelet_strength, hypoactive_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.hypoactive_strength= hypoactive_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Platelets with reduced function, leading to bleeding disorders, often seen in inherited platelet dysfunctions or drug-induced platelet inhibition. Strength: {self.hypoactive_strength} ")

          
resting= Resting_Platelets("Usman", 22, "Male", "Platelets", "Blood", "Resting Platelets", "Coagulation")
active= Active_Platelets("Usman", 22, "Male", "Platelets", "Blood", "Active Platelets", "Thrombogenicity")
large= Large_Platelets("Usman", 22, "Male", "Platelets", "Blood", "Large Platelets", "Thrombogenic")
hyperactive= Hyperactive_Platelets("Usman", 22, "Male", "Platelets", "Blood", "Hyperactive Platelets", "Thrombophilia")
hypoactive= Hypoactive_Platelets("Usman", 22, "Male", "Platelets", "Blood", "Hypoactive Platelets", "Thrombocytopenia")

print("Resting Platelets Information in Platelets")
resting.display_info()
resting.blood_function()

          
print("\n Active Platelets Information in Platelets")
active.display_info()
active.blood_function()

print("\n Large Platelets Information in Platelets")
large.display_info()
large.blood_function()

print("\n Hyperactive Platelets Information in Platelets")
hyperactive.display_info()
hyperactive.blood_function()

print("\n Hypoactive Platelets Information in Platelets")
hypoactive.display_info()
hypoactive.blood_function()

          
class Plasma(Blood):
  def __init__(self, name, age, gender, blood_name, blood_location, plasma_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.plasma_strength= plasma_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Stimulate the {self.plasma_strength} ")

class Water(Plasma):
  def __init__(self, name, age, gender, blood_name, blood_location, plasma_strength, water_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.water_strength= water_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Makes up about 90-92% of plasma and acts as a solvent for transporting nutrients, hormones, and waste products. Strength: {self.water_strength} ")

          
class Proteins(Plasma):
  def __init__(self, name, age, gender, blood_name, blood_location, plasma_strength, protein_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.protein_strength= protein_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Maintains osmotic pressure and transports molecules. Strength: {self.protein_strength} ")

          
class Electrolytes(Plasma):
  def __init__(self, name, age, gender, blood_name, blood_location, plasma_strength, electrolyte_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.electrolyte_strength= electrolyte_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Includes ions like sodium, potassium, calcium, and chloride, which help maintain pH balance, nerve function, and fluid balance. Strength: {self.electrolyte_strength} ")

class Nutrients(Plasma):
  def __init__(self, name, age, gender, blood_name, blood_location, plasma_strength, nutrient_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.nutrient_strength= nutrient_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Glucose, amino acids, fatty acids, and vitamins that are transported to tissues for energy and metabolism. Strength: {self.nutrient_strength} ")

class Steroids(Plasma):
  def __init__(self, name, age, gender, blood_name, blood_location, plasma_strength, steroid_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.steroid_strength= steroid_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Steroids regulate various bodily functions, including inflammation, immune response, metabolism, and the development of sexual characteristics. Strength: {self.steroid_strength} ")

water= Water("Usman", 22, "Male", "Plasma", "Solvent", "Plasma", "Hydration")
proteins= Proteins("Usman", 22, "Male", "Plasma", "Albumin", "Plasma", "Plasmaproteins")
electrolytes= Electrolytes("Usman", 22, "Male", "Plasma", "Suspended", "electrolytes", "Osmolarity")
nutrients= Nutrients("Usman", 22, "Male", "Plasma", "Circulation", "Plasma", "Plasmavitality")
steroids= Steroids("Usman", 22, "Male", "Plasma", "Lipids", "Plasma", "Concentration")

          
print("Water Information in Plasma")
water.display_info()
water.blood_function()

print("\n Proteins Information in Plasma")
proteins.display_info()
proteins.blood_function()

print("\n Electrolytes Information in Plasma")
electrolytes.display_info()
electrolytes.blood_function()

print("\n Nutrients Information in Plasma")
nutrients.display_info()
nutrients.blood_function()

print("\n Steroids Information in Plasma")
steroids.display_info()
steroids.blood_function()

          
class Serum(Blood):
  def __init__(self, name, age, gender, blood_name, blood_location, serum_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.serum_strength= serum_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Stimulate the {self.serum_strength} ")

class Albumin(Serum):
  def __init__(self, name, age, gender, blood_name, blood_location, serum_strength, albumin_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.albumin_strength= albumin_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Maintains osmotic pressure and transports hormones and drugs. Strength: {self.albumin_strength} ")

class Hormones(Serum):
  def __init__(self, name, age, gender, blood_name, blood_location, serum_strength, hormone_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.hormone_strength= hormone_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Includes insulin, thyroid hormones, and adrenal hormones, which regulate various physiological processes. Strength: {self.hormone_strength} ")

class Electrolytes(Serum):
  def __init__(self, name, age, gender, blood_name, blood_location, serum_strength, electrolyte_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.electrolyte_strength= electrolyte_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Includes ions like sodium, potassium, calcium, chloride, and bicarbonate, essential for nerve function, muscle contraction, and maintaining pH balance. Strength: {self.electrolyte_strength} ")

          
class Waste_Products(Serum):
  def __init__(self, name, age, gender, blood_name, blood_location, serum_strength, waste_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.waste_strength= waste_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Includes urea, creatinine, and bilirubin, which are transported to excretory organs for elimination. Strength: {self.waste_strength} ")

class Nutrients(Serum):
  def __init__(self, name, age, gender, blood_name, blood_location, serum_strength, nutrient_strength):
    super().__init__(name, age, gender, blood_name, blood_location)
    self.nutrient_strength= nutrient_strength
          
  def blood_function(self):
    print(f"{self.blood_name} Includes glucose, fatty acids, and amino acids transported in the serum to supply energy and support metabolism. Strength: {self.nutrient_strength} ")

albumin= Albumin("Usman", 22, "Male", "Serum", "Plasma", "Serum", "Albuminemia")
hormones= Hormones("Usman", 22, "Male", "Serum", "Circulation", "Serum", "Concentration")
electrolytes= Electrolytes("Usman", 22, "Male", "Serum", "Plasma", "Serum", "Concentration")
waste_products= Waste_Products("Usman", 22, "Male", "Serum", "Plasma", "Serum", "Toxicity")
nutrients= Nutrients("Usman", 22, "Male", "Serum", "Head", "Plasma", "Concentration")

print("Albumin Information in Plasma")
albumin.display_info()
albumin.blood_function()

print("\n Hormones Information in Plasma")
hormones.display_info()
hormones.blood_function()

print("\n Electrolytes Information in Plasma")
electrolytes.display_info()
electrolytes.blood_function()

print("\n Waste Products Information in Plasma")
waste_products.display_info()
waste_products.blood_function()

print("\n Nutrients Information in Plasma")
nutrients.display_info()
nutrients.blood_function()

          

red_blood_cells= Blood("Usman", 22, "Male", "Red Blood Cells", "BloodStream", "Oxygenation")
white_blood_cells= Blood("Usman", 22, "Male", "White Blood Cells", "BloodStream", "Immunity")
platelets= Blood("Usman", 22, "Male", "Platelets", "BloodStream", "Coagulation")
plasma= Blood("Usman", 22, "Male", "Plasma", "BloodStream", "Viscosity")
serum= Blood("Usman", 22, "Male", "Serum", "BloodStream", "Immunity")

print("Red Blood Cells Information in Blood")
red_blood_cells.display_info()
red_blood_cells.blood_function()

print("\n White Blood Cells Information in Blood")
white_blood_cells.display_info()
white_blood_cells.blood_function()

print("\n Platelets Information in Blood")
platelets.display_info()
platelets.blood_function()

print("\n Plasma Information in Blood")
plasma.display_info()
plasma.blood_function()

print("\n Serum Information in Blood")
serum.display_info()
serum.blood_function()