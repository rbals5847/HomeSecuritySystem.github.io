# 🏡가정 보안 시스템 Home Security System
>
> 가정용 보안 및 화재 안전 시스템



> Home Security and Fire Safety System
>
# 📄프로젝트 정보
>
> 경보 시스템 PIR 센서를 활용한 적외선 움직임 감지 시 카메라 이미지 캡쳐
>
> 화재 감지 시스템의 가스 센서(MQ-2)를 활용한 가스 감지 시 이미지 캡쳐
>
> 라즈베리파이의 Thonny와 PC화면의 p5.js에서 UART 통신을 통한 화면구현
>
> 캡쳐 이미지 저장 및 알림 확인




> Alarm System: Captures camera images when infrared motion is detected using the PIR sensor.
> 
> Fire Detection System: Captures images upon gas detection using the MQ-2 gas sensor.
> 
> Display Implementation: Uses UART communication between Thonny on Raspberry Pi and p5.js on a PC to render the display.
> 
> Image Storage & Notifications: Stores captured images and provides notification alerts.



> ### 📅제작기간 Development Time
>
>>2024.12.01 ~ 2024.12.09


> ### 🧑‍🤝‍🧑참여 인원 Number of Participants
>
>> 본인 포함 5명



>> 5 people including myself


> ### ✏️역할 Role
>
>> 코드 작성 및 업무 서포트



>>Software Development and Task Assistance

> # 🔀모델 및 구상도 System Block Diagram
>
>> ![image](https://github.com/user-attachments/assets/e3dca081-d317-4456-8b60-17dcf7bda263)

>
>> ![image](https://github.com/user-attachments/assets/18fcc6e7-0807-4dc0-a95b-f7232e677d78)




> # 🔡소프트웨어 Software
>> ![image](https://github.com/user-attachments/assets/d4f92356-480e-4d7f-9a55-a3bedadfed33)

>> ![캡처](https://github.com/user-attachments/assets/06878f02-ab06-46c3-bfd2-67ec935dbd87)


> # 🔌하드웨어 Hardware

>> CAM(GD-C100) : 사람 인식 및 확인용
>> 
>> PIR 인체감지 센서(HC-SR501) : 사람 움직임 인식
>> 
>> 피에조 부저(MH-FND) : 경보 알림
>> 
>> 가스센서(MQ-2) : 가연성 가스 센서 확인
>> 
>> 라즈베리파이(R-Pi 4) : 센서 및 통신 제어
>> 
>> HW-597 : Uart 통신



>> CAM (GD-C100): Used for human detection and verification.
>> 
>> PIR Motion Sensor (HC-SR501): Detects human movement.
>> 
>> Piezo Buzzer (MH-FND): Provides alarm notifications.
>> 
>> Gas Sensor (MQ-2): Detects flammable gases.
>> 
>> Raspberry Pi (R-Pi 4): Controls sensors and communication.
>> 
>> HW-597: Handles UART communication.

>> ![image](https://github.com/user-attachments/assets/f158ad70-c17a-4114-bf32-12cada1f8311)
>>
>> 
> # 👮침입자 감지 시스템

>>![제목 없음](https://github.com/user-attachments/assets/692f6601-86ac-4311-b07f-be7b01826baa)
>>
>> 사람이 감지되지 않을 때는 상태가 그대로 유지되지만 감지되면 침입자 발생을 알리는 빨간색 알림 표시.

>>When no person is detected, the status remains unchanged, but if a person is detected, a red alert is displayed to >>indicate an intruder.
>>
>>

> # 🔥화재 감지 시스템

>> ![image](https://github.com/user-attachments/assets/cb4d83c1-c001-48f9-ab4c-963405b9ba86)
>> 
>> 화재가 감지되지 않을 때는 상태가 그대로 유지되지만 화재가 감지되면 화재 발생을 알리는 빨간색 알림 표시.

>> When no fire is detected, the status remains unchanged, but if a fire is detected, a red alert is displayed to indicate a fire.

># 🔑소스코드

>>센서, LED 코드 - 
[코드보러가기](https://github.com/rbals5847/HomeSecuritySystem.github.io/blob/main/prj/projact.py)





















