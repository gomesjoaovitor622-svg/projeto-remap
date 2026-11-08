# REMAP Mobile

Aplicativo Flutter inicial do REMAP.

## Executar

```bash
cd mobile
flutter pub get
flutter run --dart-define=API_BASE_URL=http://10.0.2.2:8000
```

No Android Emulator, `10.0.2.2` aponta para o host. Em aparelho físico, informe o endereço HTTPS ou IP acessível da API usando `--dart-define=API_BASE_URL=...`.

O token de acesso é armazenado no armazenamento seguro do dispositivo. Ainda não há suporte offline funcional nem módulos de veículos/ECUs.
